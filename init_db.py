from db_config import get_db_connection
import sys

def init_database():
    """Initialize database with required tables"""
    conn = None
    try:
        print("Connecting to database...")
        conn = get_db_connection()
        cursor = conn.cursor()

        print("Creating tables...")
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("Users table created/verified")

        # Create customer table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                ref VARCHAR(10) PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                dob DATE,
                occupation VARCHAR(100),
                gender VARCHAR(10),
                postcode VARCHAR(20),
                mobile VARCHAR(15) UNIQUE NOT NULL,
                email VARCHAR(100),
                nationality VARCHAR(50),
                idproof VARCHAR(50),
                idnumber VARCHAR(50),
                address TEXT
            )
        """)
        print("Customer table created/verified")

        # Create room_details table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS room_details (
                floor VARCHAR(10),
                room_no VARCHAR(10) PRIMARY KEY,
                room_type VARCHAR(20)
            )
        """)
        print("Room details table created/verified")

        # Create room_booking table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS room_booking (
                contact VARCHAR(15) REFERENCES customer(mobile),
                check_in DATE,
                check_out DATE,
                room_type VARCHAR(20),
                room_no VARCHAR(10) REFERENCES room_details(room_no),
                meal VARCHAR(50),
                no_of_days INTEGER,
                meal_cost DECIMAL(10,2),
                total_bill DECIMAL(10,2)
            )
        """)
        print("Room booking table created/verified")

        # Insert default admin user if not exists
        cursor.execute("""
            INSERT INTO users (username, password, email)
            SELECT 'admin', 'admin123', 'admin@hotel.com'
            WHERE NOT EXISTS (SELECT 1 FROM users WHERE username = 'admin')
        """)
        print("Default admin user created/verified")

        conn.commit()
        print("Database initialized successfully!")
        return True
        
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    success = init_database()
    if not success:
        sys.exit(1) 