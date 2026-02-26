import pandas as pd
import os

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build correct data path
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

sentiment_path = os.path.join(DATA_DIR, "fear_greed_index.csv")
trades_path = os.path.join(DATA_DIR, "historical_data.csv")

# Load datasets
sentiment = pd.read_csv(sentiment_path)
trades = pd.read_csv(trades_path)

print("Sentiment data:")
print(sentiment.head(), "\n")

print("Trader data:")
print(trades.head())

print("\n--- SENTIMENT DATA INFO ---")
print(sentiment.info())
print("\nMissing values:\n", sentiment.isnull().sum())

print("\n--- TRADER DATA INFO ---")
print(trades.info())
print("\nMissing values:\n", trades.isnull().sum())

# ===============================
# Use Timestamp IST for trade date (FINAL)
# ===============================

trades["trade_datetime"] = pd.to_datetime(
    trades["Timestamp IST"], errors="coerce"
)

trades["trade_date"] = trades["trade_datetime"].dt.date

print("\nTrade date from IST timestamp:")
print(trades[["Timestamp IST", "trade_date"]].head())

# ===============================
# Merge trader data with sentiment
# ===============================

# Ensure sentiment date is date type
sentiment["date"] = pd.to_datetime(sentiment["date"]).dt.date

merged = trades.merge(
    sentiment[["date", "classification"]],
    left_on="trade_date",
    right_on="date",
    how="left"
)

print("\nMerged data sample:")
print(merged[["trade_date", "classification"]].head())

# ============================
# PnL vs Sentiment Analysis
# ============================

pnl_by_sentiment = (
    merged
    .groupby("classification")["Closed PnL"]
    .mean()
    .reset_index()
)

print("\nAverage PnL by Sentiment:")
print(pnl_by_sentiment)

trade_count = merged["classification"].value_counts()
print("\nTrade count by sentiment:")
print(trade_count)

print(merged[["classification", "Closed PnL"]].head())

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.bar(pnl_by_sentiment["classification"], pnl_by_sentiment["Closed PnL"])
plt.xlabel("Market Sentiment")
plt.ylabel("Average Closed PnL")
plt.title("Average PnL by Market Sentiment")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("output/pnl_vs_sentiment.png")
plt.show()
# Win rate calculation
merged["win"] = merged["Closed PnL"] > 0

win_rate = (
    merged
    .groupby("classification")["win"]
    .mean()
    .reset_index()
)

print("\nWin Rate by Sentiment:")
print(win_rate)

win_rate["win_rate_percent"] = win_rate["win"] * 100
print("\nWin Rate (%) by Sentiment:")
print(win_rate[["classification", "win_rate_percent"]])