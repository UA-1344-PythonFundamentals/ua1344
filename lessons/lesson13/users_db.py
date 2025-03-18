import sqlite3
from faker import Faker
import datetime

def create_user_table(database_path):
    """
    Creates a 'users' table in an SQLite database.

    Args:
        database_path (str): The path to the SQLite database file.
    """
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                first_name TEXT,
                last_name TEXT,
                date_of_birth DATE,
                is_active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        print(f"Table 'users' created successfully in {database_path}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()

def generate_and_insert_users(database_path, num_users=10):
    """
    Generates and inserts a specified number of fake user records into the 'users' table.

    Args:
        database_path (str): The path to the SQLite database file.
        num_users (int, optional): The number of users to generate. Defaults to 10.
    """
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        fake = Faker()

        for _ in range(num_users):
            profile = fake.simple_profile()
            username = profile['username']
            email = profile['mail']
            password = fake.password()  # Store securely in a real application!
            print(profile)
            first_name = profile['username']
            last_name = profile['name'].split(' ')[-1] # Extract last name

            # Generate a random date of birth
            start_date = datetime.date(1950, 1, 1)
            end_date = datetime.date(2005, 12, 31)  # Assuming users are at least 18
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = fake.random_int(min=0, max=days_between_dates)
            date_of_birth = start_date + datetime.timedelta(days=random_number_of_days)

            is_active = fake.random_element(elements=(0, 1))

            cursor.execute('''
                INSERT INTO users (username, email, password, first_name, last_name, date_of_birth, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (username, email, password, first_name, last_name, date_of_birth, is_active))

        conn.commit()
        print(f"{num_users} users generated and inserted into {database_path}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()

database_file = "user_database.db"
if __name__ == "__main__":
    # Main execution
    
    # create_user_table(database_file)  # Create the table first (if it doesn't exist)
    generate_and_insert_users(database_file, num_users=10)