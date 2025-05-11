# Import the QueryBase class
#### YOUR CODE HERE #DONE
from sqlite3 import connect
import query_base
import pandas as pd
import query_base


# Import dependencies needed for sql execution
# from the `sql_execution` module
#### YOUR CODE HERE #Done
import sql_execution
# Define a subclass of QueryBase
# called Employee
#### YOUR CODE HERE #DONE
class Employee(query_base):
    # Set the class attribute `name`
    # to the string "employee"
    #### YOUR CODE HERE #DONE
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE #DONE
    def names(self):

        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        #### YOUR CODE HERE #DONE
        connection = connect(sql_execution.db_path)
        # cursor =  connection.cursor()
        SQL_query = f""" 
        SELECT 
            first_name,
            last_name,
            employee_id 
        FROM employee
        """

        # cursor.execute(SQL_query)
        df_employee = pd.read_sql_query(SQL_query)
        return df_employee
    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE #DONE
    def username(self, id):
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        #### YOUR CODE HERE #DONE

        connection = connect(sql_execution.db_path)
        # cursor =  connection.cursor()
        SQL_query = f""" 
        SELECT 
            first_name,
            last_name,
        FROM employee
        WHERE employee_id = %s
        """ % (id)
        # cursor.execute(SQL_query)
        df_employee_name = pd.read_sql_query(SQL_query)
        return df_employee_name
    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE #DONE
    def model_data(self, id):
        query = f"""
                    SELECT SUM(positive_events) positive_events
                            , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """
        df_query_result = pd.read_sql_query(query)
        # return pd.read_sql_query(query)
        return df_query_result