#!/usr/bin/env python3
"""
A Python script that creates the database 'alx_book_store' in a MySQL server.

- The script takes no arguments.
- It connects to a MySQL server on localhost (port 3306).
- If the database 'alx_book_store' already exists, the script does not fail.
- The script does not use any 'SELECT' or 'SHOW' statements.
"""

import mysql.connector
from mysql.connector import Error
import sys

# --- Database Connection Parameters ---
# !!! IMPORTANT !!!
# Replace 'your_username' and 'your_password' with your actual MySQL credentials.
# For the ALX environment, this is typically 'root' and 'root'.
db_config = {
    'host': 'localhost',
    'user': 'your_username',  # e.g., 'root'
    'password': 'your_password' # e.g., 'root'
}
# --------------------------------------

def create_database():
    """
    Connects to MySQL server and creates the 'alx_book_store' database
    if it does not already exist.
    """
    db_conn = None
    cursor = None

    try:
        # 1. Establish a connection to the MySQL server
        db_conn = mysql.connector.connect(**db_config)
        cursor = db_conn.cursor()

        # 2. Try to create the database
        try:
            # We run the command without 'IF NOT EXISTS'
            # This allows us to catch the specific error if it exists,
            # and only print success if it was newly created.
            cursor.execute("CREATE DATABASE alx_book_store")
            
            # 3. Print success message (as required)
            # This line only runs if the 'execute' above was successful
            print("Database 'alx_book_store' created successfully!")
            
        except mysql.connector.Error as err:
            # 4. Handle errors
            # Error code 1007: Can't create database '...'; database exists
            if err.errno == 1007:
                # Per instructions, do not fail if it exists.
                # We can silently pass.
                pass
            else:
                # If it's a different error, print it
                print(f"Failed to create database: {err}", file=sys.stderr)

    except mysql.connector.Error as conn_err:
        # 5. Handle connection errors
        print(f"Error connecting to MySQL: {conn_err}", file=sys.stderr)
        
    finally:
        # 6. Handle open and close of the DB connection
        if cursor:
            cursor.close()
        if db_conn:
            db_conn.close()

if __name__ == "__main__":
    create_database()
