import csv
import sqlite3
import os
import pandas as pd


#pathing
curated_csv_path = os.path.join("data", "curated_emails.csv")
fake_csv_path = os.path.join("data", "fake_emails.csv")
database_path = os.path.join("database", "data_lux.db")

os.makedirs("database", exist_ok=True)
conn = sqlite3.connect(database_path)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    subject TEXT,
    body TEXT,
    date TEXT
    )"""
)

def load_csv_into_db(csv_file_path):
    with open(csv_file_path, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cur.execute("""
            INSERT INTO emails (sender,subject,body,date) VALUES (?,?,?,?)""",
                        (row['sender'], row['subject'], row['body'], row['date']))

load_csv_into_db(curated_csv_path)
load_csv_into_db(fake_csv_path)

conn.commit()
cur.close()
conn.close()

print("All emails loaded successfully!")