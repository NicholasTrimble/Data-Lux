import sqlite3
from textblob import TextBlob


database_path = "database/data_lux.db"
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

#add new columns
cursor.execute("ALTER TABLE emails ADD COLUMN sentiment TEXT")
cursor.execute("ALTER TABLE emails ADD COLUMN email_type TEXT")

#using textblob to get user sentiment
def classify_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"


def classify_email_type(text):
    text_lower = text.lower()

    if "suggest" in text_lower or "would be nice" in text_lower:
        return "suggestion"
    elif "complain" in text_lower or "crash" in text_lower or "fail" in text_lower:
        return "complaint"
    else:
        return "feedback"

#get the emails
cursor.execute("SELECT id, body FROM emails")
emails = cursor.fetchall()

#process emails
for email_id, body_text in emails:
    sentiment_result = classify_sentiment(body_text)
    email_type_result = classify_email_type(body_text)

    # UPDATE DATABASE
    cursor.execute("""
    UPDATE emails
    SET sentiment = ?, email_type = ?
    WHERE id = ?
    """, (sentiment_result, email_type_result, email_id))

#close
connection.commit()
cursor.close()
connection.close()

print("NLP classification complete! Sentiment and email_type columns updated.")
