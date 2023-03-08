import mysql.connector
from flask import Flask, request
from datetime import datetime

app = Flask("Email Tracker")

DB_NAME = "emailtracker"
DB_USER = "admin"
DB_PASSWORD = "Admin123"
DB_HOST = "email-tracker.cs3lpdyuw6nm.us-east-1.rds.amazonaws.com"
DB_PORT = "3306"

conn = mysql.connector.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

if conn.is_connected():
    print("Connected to MySQL database")

@app.route('/track', methods=['GET'])
def track_email():
    email_id = request.args.get('email_id')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM email_tracking WHERE email_id=%s", (email_id,))
    result = cursor.fetchone()
    if result:
        # if email_id exists, update count and time
        count = result[2] + 1
        cursor.execute("UPDATE email_tracking SET count=%s, last_opened=%s WHERE email_id=%s", (count, datetime.now(), email_id))
    else:
        # if email_id does not exist, add new row
        count = 1
        cursor.execute("INSERT INTO email_tracking (email_id, count, last_opened) VALUES (%s, %s, %s)", (email_id, count, datetime.now()))
    conn.commit()
    cursor.close()
    return {'message': 'Email tracked successfully.'}
