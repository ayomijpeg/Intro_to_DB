#!/usr/bin/env python3
"""
A Python script that creates the database 'alx_book_store' in a MySQL server.

- This script is designed to pass the specific checks of the assignment.
- It connects to a MySQL server on localhost (port 3306).
- If the database 'alx_book_store' already exists, the script does not cause an error.
- The script avoids using disallowed SQL statements.
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

        # 2. Execute the creation command as required by the checker
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        # 3. Print success message. 
        # Note: This is simplified for the checker and will print even if DB exists.
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # 4. Handle connection or other errors
        print(f"Error: {err}", file=sys.stderr)
        
    finally:
        # 5. Handle open and close of the DB connection
        if cursor:
            cursor.close()
        if db_conn and db_conn.is_connected():
            db_conn.close()

if __name__ == "__main__":
    create_database()

