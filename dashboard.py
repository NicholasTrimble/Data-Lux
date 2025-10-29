import sqlite3

import pandas as pd
import streamlit as st


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
st.bar_chart(sentiment_counts)

st.subheader("Recent Emails")
st.dataframe(filtered_df[['sender','subject','sentiment','email_type','date']].sort_values(by='date', ascending=False))