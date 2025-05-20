import os
import sys
from tkinter import Tk, messagebox
from login import Login_Window
from db_config import get_db_connection
from init_db import init_database

class HotelManagementSystem:
    def __init__(self):
        self.root = Tk()
        self.setup_environment()
        self.start_application()

    def setup_environment(self):
        """Setup application environment"""
        try:
            # Create images directory if it doesn't exist
            if not os.path.exists('images'):
                os.makedirs('images')
                messagebox.showwarning("Warning", "Images directory created. Please add required images.")

            # Initialize database
            print("Initializing database...")
            if not init_database():
                messagebox.showerror("Error", "Database initialization failed. Please check the console for details.")
                sys.exit(1)

            # Test database connection
            print("Testing database connection...")
            conn = get_db_connection()
            conn.close()
            print("Database connection successful!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Setup failed: {str(e)}")
            sys.exit(1)

    def start_application(self):
        """Start the application with login window"""
        try:
            self.root.withdraw()  # Hide main window
            login_window = Login_Window(self.root)
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Application failed to start: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    app = HotelManagementSystem() 