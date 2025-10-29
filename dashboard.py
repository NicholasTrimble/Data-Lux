import sqlite3
import pandas as pd
import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

connection = sqlite3.connect("database/data_lux.db")
emails_df = pd.read_sql_query("SELECT * FROM emails", connection)
connection.close()

st.title("Data Lux")
st.write("Visualizing SMART email insights")

email_types = emails_df['email_type'].unique().tolist()
selected_type = st.selectbox("Filter by email type", ["ALL"] + email_types)

if selected_type != "ALL":
    filtered_df = emails_df[emails_df['email_type'] == selected_type]
else:
    filtered_df = emails_df

sentiment_counts = filtered_df["sentiment"].value_counts()
st.subheader("Sentiment Distribution")
st.bar_chart(sentiment_counts)

st.subheader("Recent Emails")
st.dataframe(
    filtered_df[['sender', 'subject', 'sentiment', 'email_type', 'date']].sort_values(by='date', ascending=False)
)

st.subheader("Ask Questions About Emails")
user_question = st.text_input("Enter your question here:")

if st.button("Get AI Answer") and user_question:
    prompt = f"""
    You are an assistant analyzing a database of emails with columns:
    sender, subject, body, date, sentiment, email_type.
    The user asked: "{user_question}"
    Provide a concise answer using the database information.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0
        )
        st.write("AI Answer:")
        st.write(response.choices[0].text.strip())
    except Exception as e:
        st.error(f"Error fetching AI response: {e}")
