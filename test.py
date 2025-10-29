import sqlite3
#
# connection = sqlite3.connect("database/data_lux.db")
# cursor = connection.cursor()
# cursor.execute("SELECT COUNT(*) FROM emails")
# total_rows = cursor.fetchone()[0]
# print(f"Total emails in database: {total_rows}")
# cursor.execute("SELECT * FROM emails LIMIT 5")
# for row in cursor.fetchall():
#     print(row)
# connection.close()


conn = sqlite3.connect("database/data_lux.db")
cursor = conn.cursor()
cursor.execute("SELECT sender, subject, sentiment, email_type FROM emails LIMIT 10")
for row in cursor.fetchall():
    print(row)
conn.close()
