# Import any dependencies needed to execute sql queries
# YOUR CODE HERE #DONE
import psycopg2
import sqlite3
import mysql.connector
from sqlalchemy import create_engine, text
import pandas as pd
# from pathlib import Path
import sql_execution


# db_path = Path(__file__).resolve().parent / 'employee_events.db'
# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase(sql_execution):
    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE #DONE
    name = ""
    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE #DONE
    def names():
        nameList = []
        return nameList
        # Return an empty list
        # YOUR CODE HERE #DONE


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE 
    def event_counts(id):
        df = pd.DataFrame()       
        # joiningColumn = 
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE #DONE
        
        connection = sqlite3.connect(sql_execution.db_path)
        # cursor =  connection.cursor()
        SQL_query = f""" 
        SELECT 
            event_date,
            SUM(positive_events),
            SUM(negative_events) 
        FROM employee_events
        GROUP BY event_date
        ORDER BY event_date;
        """

        # cursor.execute(SQL_query)
        df = pd.read_sql_query(SQL_query, connection)
        return df
    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE
    def notes(id):
        df = pd.DataFrame()

     
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE #DONE
        connection = sqlite3.connect("employee_events.db")
        # cursor =  connection.cursor()
        SQL_query = f""" 
        SELECT 
            notes,
            note_date
        FROM notes
        """ 
        # cursor.execute(SQL_query)
        df = pd.read_sql_query(SQL_query, connection)
        return df

