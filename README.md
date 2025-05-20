# Hotel Management System

A comprehensive hotel management system built with Python and PostgreSQL, featuring a modern GUI interface using Tkinter.

## Features

- User Authentication (Login/Register)
- Customer Management
- Room Booking and Management
- Room Details Management
- Search Functionality
- Modern GUI Interface
- PostgreSQL Database Integration

## System Requirements
- Windows 10 or later
- MySQL Server 8.0 or later
- 4GB RAM minimum
- 500MB free disk space

## Installation Instructions

### Automatic Installation
1. Run `install.bat` as administrator
2. Follow the on-screen instructions
3. The installer will:
   - Install Python if not present
   - Install required packages
   - Set up the database
   - Create the executable

### Manual Installation
1. Install Python 3.9 or later
2. Install MySQL Server 8.0 or later
3. Run `pip install -r requirements.txt`
4. Run `mysql -u root -p < database/setup_database.sql`
5. Run `python setup.py build`

## First Time Setup
1. Launch the application
2. Register a new admin account
3. Log in with your credentials

## Database Configuration
- Default MySQL username: root
- Default MySQL password: (set during MySQL installation)
- Database name: hotel_management

## Support
For any issues or questions, please contact support@yourdomain.com 