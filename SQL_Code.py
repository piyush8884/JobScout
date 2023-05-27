import json
import sqlite3
import datetime
import time


# Load JSON data
def insert_json_into_database():

    with open('job_data.json', 'r') as file:
        json_data = json.load(file)

    # Connect to SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        key_column TEXT,
                        value_column TEXT,
                        timestamp DATETIME
                    )''')
    current_time = datetime.datetime.now()
    # Iterate over JSON data and insert records into the table
    for key,value in json_data.items():
        cursor.execute("INSERT INTO my_table (key_column, value_column,timestamp) VALUES (?, ?, ?)",
                       (key, value,current_time))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
insert_json_into_database()
