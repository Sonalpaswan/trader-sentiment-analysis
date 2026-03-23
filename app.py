import streamlit as st
import pandas as pd

st.title("Trader Sentiment Analysis 📊")

st.write("This app analyzes trader sentiment based on Fear & Greed Index")

# Example load
df = pd.read_csv("data/your_file.csv")  # apni file ka naam dalna

st.write(df.head())

st.bar_chart(df.select_dtypes(include=['number']))
