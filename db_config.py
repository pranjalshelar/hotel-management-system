import mysql.connector
from tkinter import messagebox
import sys

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'pranjal,321',  # Your MySQL password
    'database': 'management',
    'raise_on_warnings': True
}

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        if err.errno == 1045:  # Access denied error
            messagebox.showerror("Error", "Access denied. Please check your MySQL username and password.")
        elif err.errno == 1049:  # Unknown database error
            messagebox.showerror("Error", "Database 'management' does not exist. Please create it first.")
        elif err.errno == 2003:  # Can't connect to server
            messagebox.showerror("Error", "Cannot connect to MySQL server. Please check if MySQL is running.")
        else:
            messagebox.showerror("Error", f"Database error: {str(err)}")
        return None

def execute_query(query, params=None, fetch=False):
    """Execute a query and optionally fetch results"""
    conn = get_db_connection()
    if not conn:
        return None
    
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
            
        if fetch:
            result = cursor.fetchall()
        else:
            conn.commit()
            result = True
            
        cursor.close()
        conn.close()
        return result
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Query execution error: {str(err)}")
        if conn:
            conn.close()
        return None 