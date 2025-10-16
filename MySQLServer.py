#!/usr/bin/env python3
"""
MySQLServer.py - Script to create alxbookstore database
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the alxbookstore database in MySQL server
    """
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database alxbookstore if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
            
            print("Database 'alxbookstore' created successfully!")
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        # Close connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
