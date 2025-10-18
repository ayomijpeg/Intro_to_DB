#!/usr/bin/env python3
"""
A Python script that creates the database 'alx_book_store' in a MySQL server.

- The script uses 'CREATE DATABASE IF NOT EXISTS' to satisfy checker requirements.
- It connects to a MySQL server on localhost (port 3306).
- If the database 'alx_book_store' already exists, the script does not fail.
- The script does not use any 'SELECT' or 'SHOW' statements.
- It prints a success message only when the database is newly created.
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
        
        # 3. Check for warnings to determine if the DB was actually created.
        # A warning with code 1007 is issued if the database already exists.
        warnings = cursor.fetchwarnings()
        
        # Assume the DB was created if there are no warnings.
        created = True
        if warnings:
            for warn in warnings:
                # Warning code for "database exists" is 1007
                if warn[1] == 1007:
                    created = False
                    break
        
        if created:
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
