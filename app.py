import streamlit as st
import pandas as pd   # 👈 ye add karo

st.title("Trader Sentiment Analysis 📊")

st.write("This app analyzes trader sentiment based on Fear & Greed Index")

# 👉 YAHI ADD KARNA HAI (DATA LOAD)
df = pd.read_csv("fear_greed_index.csv")

# 👉 Data show karo
st.subheader("Dataset Preview")
st.write(df.head())

# 👉 Graph show karo (automatic numeric columns)
st.subheader("Data Visualization")
st.bar_chart(df.select_dtypes(include=['number']))

st.header("Features")
st.write("""
- Analyze market sentiment  
- Study trader performance  
- Understand trading patterns  
""")

st.success("App successfully deployed 🚀")
