from fasthtml.common import *
from fasthtml import *
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import numpy as np
import sys

# Import QueryBase, Employee, Team from employee_events
#### YOUR CODE HERE #DONE
project_root = Path().resolve().parent.parent
sys.path.append(str(project_root))
from python_package import QueryBase, Employee, Team

# import the load_model function from the utils.py file
#### YOUR CODE HERE #DONE
from utils import load_model

"""
Below, we import the parent classes
you will use for subclassing
"""
from base_components import (
    Dropdown,
    BaseComponent,
    Radio,
    MatplotlibViz,
    DataTable
    )

from combined_components import FormGroup, CombinedComponent

# from src import 

project_root = Path(__file__).root.absolute()
# Create a subclass of base_components/dropdown
# called `ReportDropdown`
#### YOUR CODE HERE #DONE
class ReportDropdown(Dropdown):
        
    # Overwrite the build_component method
    # ensuring it has the same parameters
    # as the Report parent class's method
    #### YOUR CODE HERE
    def build_component(self, entity_id, model):
        super().build_component(entity_id, model)
        # return super().build_component(entity_id, model)

        #  Set the `label` attribute so it is set
        #  to the `name` attribute for the model
        #### YOUR CODE HERE #DONE
        self.label = model.name

        # Return the output from the
        # parent class's build_component method
        #### YOUR CODE HERE #DONE
        return super().build_component(entity_id, model)

    # Overwrite the `component_data` method
    # Ensure the method uses the same parameters
    # as the parent class method
    #### YOUR CODE HERE 
    def component_data(self, entity_id, model):
        super().component_data(entity_id, model)
        # Using the model argument
        # call the employee_events method
        # that returns the user-type's
        # names and ids   

# Create a subclass of base_components/BaseComponent
# called `Header`
#### YOUR CODE HERE #DONE
class Header(BaseComponent):
    # Overwrite the `build_component` method
    # Ensure the method has the same parameters
    # as the parent class
    #### YOUR CODE HERE #DONE
    def build_component(self, entity_id, model):
        super().build_component(entity_id, model)
        # Using the model argument for this method
        # return a fasthtml H1 objects
        # containing the model's name attribute
        #### YOUR CODE HERE #DONE
        H1(model.name)

# Create a subclass of base_components/MatplotlibViz
# called `LineChart`
#### YOUR CODE HERE #DONE
class LineChart(MatplotlibViz):    
    # Overwrite the parent class's `visualization`
    # method. Use the same parameters as the parent
    #### YOUR CODE HERE #DONE
    def visualization(self, entity_id, model):
        super().visualization(entity_id, model)
        # Pass the `asset_id` argument to
        # the model's `event_counts` method to
        # receive the x (Day) and y (event count)
        #### YOUR CODE HERE
        df = pd.DataFrame( model.event_counts(entity_id) )

        # Use the pandas .fillna method to fill nulls with 0
        #### YOUR CODE HERE
        df_noZeros = df.fillna(0)

        # Use the pandas .set_index method to set
        # the date column as the index
        #### YOUR CODE HERE #DONE
        df_noZeros.set_index('date', inplace=True)

        # Sort the index
        #### YOUR CODE HERE #DONE
        df_noZeros.sort_index(inplace=True)

        # Use the .cumsum method to change the data
        # in the dataframe to cumulative counts
        #### YOUR CODE HERE #DONE
        cumm_df = df_noZeros.cumsum
        
        # Set the dataframe columns to the list
        # ['Positive', 'Negative']
        #### YOUR CODE HERE #DONE
        df_noZeros.columns = ['Positive', 'Negative']

        # Initialize a pandas subplot
        # and assign the figure and axis
        # to variables
        #### YOUR CODE HERE #DONE
        figure, axis = plt.subplots()

        # call the .plot method for the
        # cumulative counts dataframe
        #### YOUR CODE HERE #DONE
        cumm_df.plot(ax=axis)

        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        # Use keyword arguments to set 
        # the border color and font color to black. 
        # Reference the base_components/matplotlib_viz file 
        # to inspect the supported keyword arguments
        #### YOUR CODE HERE #DONE
        self.set_axis_styling(axis, 'black', 'black')

        # Set title and labels for x and y axis
        #### YOUR CODE HERE #DONE
        axis.set_xlabel('date')
        axis.set_ylabel('cumulative counts')

# Create a subclass of base_components/MatplotlibViz
# called `BarChart`
#### YOUR CODE HERE #DONE
class BarChart(MatplotlibViz):
    # Create a `predictor` class attribute
    # assign the attribute to the output
    # of the `load_model` utils function
    #### YOUR CODE HERE #DONE
    predictor = load_model()

    # Overwrite the parent class `visualization` method
    # Use the same parameters as the parent
    #### YOUR CODE HERE
    def visualization(self, entity_id, model):
        super().visualization(entity_id, model)
        # Using the model and asset_id arguments
        # pass the `asset_id` to the `.model_data` method
        # to receive the data that can be passed to the machine
        # learning model
        #### YOUR CODE HERE #DONE
        data = Team.model_data(self,entity_id)
        
        # Using the predictor class attribute
        # pass the data to the `predict_proba` method
        #### YOUR CODE HERE #DONE
        self.predictor =  model.predict_proba(data)

        # Index the second column of predict_proba output
        # The shape should be (<number of records>, 1)
        #### YOUR CODE HERE #DONE
        second_col = model.predict_proba(data)[:,1]
        
        # Below, create a `pred` variable set to
        # the number we want to visualize
        #
        # If the model's name attribute is "team"
        # We want to visualize the mean of the predict_proba output
        #### YOUR CODE HERE #DONE
        if model.name == "team":
            pred = np.mean(second_col)

        # Otherwise set `pred` to the first value
        # of the predict_proba output
        #### YOUR CODE HERE #DONE
        else:
            pred = second_col[0]

        # Initialize a matplotlib subplot
        #### YOUR CODE HERE #DONE
        plt.su
        fig, ax = plt.subplot(1,1)
        
        # Run the following code unchanged
        ax.barh([''], [pred])
        ax.set_xlim(0, 1)
        ax.set_title('Predicted Recruitment Risk', fontsize=20)
        
        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        #### YOUR CODE HERE #DONE
        self.set_axis_styling(ax)
# Create a subclass of combined_components/CombinedComponent
# called Visualizations       
#### YOUR CODE HERE #DONE 
class Visulizations(CombinedComponent):
        
    # Set the `children`
    # class attribute to a list
    # containing an initialized
    # instance of `LineChart` and `BarChart`
    #### YOUR CODE HERE #DONE
        Lchart = LineChart()
        Bchart = BarChart()
        children = [
            Lchart.__init__(),
            Bchart.__init__()
        ]

    # Leave this line unchanged
        outer_div_type = Div(cls='grid')
            
# Create a subclass of base_components/DataTable
# called `NotesTable`
#### YOUR CODE HERE #DONE
class NotesTable(DataTable):


    # Overwrite the `component_data` method
    # using the same parameters as the parent class
    #### YOUR CODE HERE #DONE
        def component_data(self, entity_id, model):
            super().component_data(entity_id, model)

        # Using the model and entity_id arguments
        # pass the entity_id to the model's .notes 
        # method. Return the output
        #### YOUR CODE HERE #DONE
            return model.notes(entity_id)

class DashboardFilters(FormGroup):

    id = "top-filters"
    action = "/update_data"
    method="POST"

    children = [
        Radio(
            values=["Employee", "Team"],
            name='profile_type',
            hx_get='/update_dropdown',
            hx_target='#selector'
            ),
        ReportDropdown(
            id="selector",
            name="user-selection")
        ]
    
# Create a subclass of CombinedComponents
# called `Report`
#### YOUR  CODE HERE #DONE
class Report(CombinedComponent):
    # Set the `children`
    # class attribute to a list
    # containing initialized instances 
    # of the header, dashboard filters,
    # data visualizations, and notes table
    #### YOUR CODE HERE #DONE
    H = Header()
    DBFilter = DashboardFilters()
    dv = Visulizations
    children = [
        H.__init__(),
        DBFilter.__init__(),
        dv.__init__()
        ]
# Initialize a fasthtml app 
#### YOUR CODE HERE #DONE  
    app = FastHTML()

# Initialize the `Report` class
#### YOUR CODE HERE #DONE

    def __init__(self, ID, Employee):
        self.ID = ID
        self.Employee = Employee

# Create a route for a get request
# Set the route's path to the root
#### YOUR CODE HERE #DONE
    @app.route(project_root)
    def get():
        # Call the initialized report
        # pass the integer 1 and an instance
        # of the Employee class as arguments
        # Return the result
        #### YOUR CODE HERE #DONE
        emp = Employee()
        result = Report(1, emp)
        return result

# Create a route for a get request
# Set the route's path to receive a request
# for an employee ID so `/employee/2`
# will return the page for the employee with
# an ID of `2`. 
# parameterize the employee ID 
# to a string datatype
#### YOUR CODE HERE
    @app.route('/employee/<string:id>')
    def get(id:str):
    # Call the initialized report
    # pass the ID and an instance
    # of the Employee SQL class as arguments
    # Return the result
    #### YOUR CODE HERE
        emp = Employee()
        result = Report(id, emp)
        return result

# Create a route for a get request
# Set the route's path to receive a request
# for a team ID so `/team/2`
# will return the page for the team with
# an ID of `2`. 
# parameterize the team ID 
# to a string datatype
#### YOUR CODE HERE
    @app.route('/team/<string:id>')
    def get(id:str):

    # Call the initialized report
    # pass the id and an instance
    # of the Team SQL class as arguments
    # Return the result
    #### YOUR CODE HERE
        team = Team()
        result = Report(id, team)
        return result


# Keep the below code unchanged!
@app.get('/update_dropdown{r}')
def update_dropdown(r):
    dropdown = DashboardFilters.children[1]
    print('PARAM', r.query_params['profile_type'])
    if r.query_params['profile_type'] == 'Team':
        return dropdown(None, Team())
    elif r.query_params['profile_type'] == 'Employee':
        return dropdown(None, Employee())


@app.post('/update_data')
async def update_data(r):
    from fasthtml.common import RedirectResponse
    data = await r.form()
    profile_type = data._dict['profile_type']
    id = data._dict['user-selection']
    if profile_type == 'Employee':
        return RedirectResponse(f"/employee/{id}", status_code=303)
    elif profile_type == 'Team':
        return RedirectResponse(f"/team/{id}", status_code=303)
    


serve()
