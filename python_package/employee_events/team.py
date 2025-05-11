# Import the QueryBase class
import query_base
# YOUR CODE HERE #DONE

# Import dependencies for sql execution
#### YOUR CODE HERE #DONE
from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

db_path = Path(__file__).resolve().parent / 'employee_events.db'
# Create a subclass of QueryBase
# called  `Team`
#### YOUR CODE HERE  #DONE
class Team(query_base):
    def __init__(self):
        connection = "asdf"
    def setter():
        global connection 
        connection = connect(db_path)
    # Set the class attribute `name`
    # to the string "team"
    #### YOUR CODE HERE #DONE
    name = "team"
    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    #### YOUR CODE HERE #DONE
    def names ():
        result_list = []
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        #### YOUR CODE HERE

        cursor =  connection.cursor()
        SQL_query = f""" 
        SELECT 
            team_id,
        FROM employee
        WHERE team_id = {ID}
        """
        cursor.execute(SQL_query)

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    #### YOUR CODE HERE #DONE
    def username(ID):
        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
        #### YOUR CODE HERE #DONE

        # connection = connect(db_path)
        cursor =  connection.cursor()
        SQL_query = f""" 
        SELECT 
            team_id,
        FROM employee
        WHERE team_id = {ID}
        """
        cursor.execute(SQL_query)
        result_list = cursor.fetchall()
        return result_list
    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE #DONE

    def model_data(self, id):
        connection = connect(db_path)
        # cursor =  connection.cursor()
        SQL_query = f"""
            SELECT positive_events, negative_events FROM (
                    SELECT employee_id
                         , SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                    GROUP BY employee_id
                   )
                """
        df = pd.read_sql_query(SQL_query, connection)
        pd.read_sql
        return df