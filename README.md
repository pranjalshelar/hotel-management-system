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

## Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd hotel-management-system
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL:
   - Install PostgreSQL if not already installed
   - Create a new database named 'hotel_management'
   - Update the database configuration in the code if needed

5. Run the application:
```bash
python login.py
```

## Project Structure

```
hotel-management-system/
├── images/              # Image assets
├── login.py            # Login window
├── register.py         # Registration window
├── HMS.py             # Main application window
├── customer.py         # Customer management
├── room.py            # Room booking
├── details.py         # Room details
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Database Configuration

The application uses PostgreSQL. Update the database configuration in the code:

```python
DB_CONFIG = {
    'host': 'localhost',
    'database': 'hotel_management',
    'user': 'postgres',
    'password': 'your_password',
    'port': '5432'
}
```

## Usage

1. Start the application by running `login.py`
2. Login with your credentials or register a new account
3. Use the main interface to:
   - Manage customers
   - Book rooms
   - View room details
   - Search records

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers. 