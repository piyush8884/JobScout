
import json
import sqlite3
import time
from twilio.rest import Client
def Job_links():
# Set up Twilio credentials
    account_sid = ''
    auth_token = ''
    twilio_phone_number = ''
    receiver_phone_number = ''

    # Connect to SQLite3 database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Query the first 3 job entries from the database
    cursor.execute("SELECT key_column ,value_column FROM my_table LIMIT 3")
    job_entries = cursor.fetchall()

    # Compose the message with job data
    message = "This is the Latest Job Openings on Linkdln\n"
    for title, url in job_entries:
        message += f"{title}: {url}\n"

    # Send SMS using Twilio
    client = Client(account_sid, auth_token)
    sms = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=receiver_phone_number
    )

    # Print SMS SID to confirm successful sending
    print(sms.sid)

    # Close the database connection
    conn.close()

    # Wait for 24 hours before sending the next batch of job links
    time.sleep(24 * 60 * 60)
Job_links()

