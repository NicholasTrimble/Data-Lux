import sqlite3
from collections import Counter

connection = sqlite3.connect("database/data_lux.db")
cursor = connection.cursor()

cursor.execute("SELECT email_type, Count(*) FROM emails GROUP BY email_type")
type_counts = cursor.fetchall()
print("Email Type Counts:")
for email_type, count in type_counts:
    print(f"{email_type}: {count}")

cursor.execute("SELECT sentiment, COUNT(*) FROM emails group by sentiment")
sentiment_counts = cursor.fetchall()
print("\nSentiment Counts:")
for sentiment, count in sentiment_counts:
    print(f"{sentiment}: {count}")

cursor.execute("SELECT body FROM emails")
all_bodies = cursor.fetchall()
words = []
for (body,) in all_bodies:
    words.extend(body.lower().split())
word_counts = Counter(words)
top_keywords = word_counts.most_common(10)
print("\nTop 10 Keywords:")
for word, count in top_keywords:
    print(f"{word}: {count}")

cursor.close()
connection.close()