# Trader Sentiment Analysis

This project was completed as part of a Data Science Intern assignment focusing on trader behavior vs market sentiment.
# Trader Sentiment Analysis

This project analyzes how market sentiment (Fear & Greed Index) impacts trader behavior and performance.
The goal is to study changes in PnL, win rate, leverage usage, and trading frequency under different market sentiments.

## Datasets Used

### Fear & Greed Index
- Sentiment score (0–100)
- Classification: Extreme Fear, Fear, Neutral, Greed, Extreme Greed
- Daily date extracted from timestamp

### Trader Historical Data
- Trade execution details
- Closed PnL
- Trade size, leverage, side (Long/Short)
- Timestamp converted to daily date

## Part A — Data Preparation

- Loaded both datasets and inspected structure
- Checked missing values and duplicates
- Converted timestamps to daily dates
- Merged trader data with sentiment data on date
- Created key metrics:
  - Daily PnL
  - Win rate
  - Trade frequency
  - Long/Short ratio
  - Leverage behavior

  ## Part B — Analysis

### Key Findings
- Average PnL is higher during Greed and Extreme Greed periods
- Win rate drops during Extreme Fear
- Traders reduce trade frequency during Fear phases
- Leverage usage increases during Greed

### Visual Analysis
- Bar chart showing Average PnL by Market Sentiment
- Trade count distribution across sentiment categories

## Part C — Actionable Insights

### Strategy Rules
1. During Fear periods, reduce leverage and trade selectively
2. Avoid high leverage during Extreme Greed to control drawdowns
3. Increase trade frequency only when sentiment is stable (Neutral/Greed)

## Bonus Work

- Sentiment-based trader segmentation
- Performance comparison across trader types
- Saved visual outputs for reporting

## Project Structure

trader-sentiment-assignment/
├── data/
│   ├── fear_greed_index.csv
│   └── historical_data.csv
├── notebook/
│   ├── analysis.py
│   └── analysis.ipynb
├── output/
│   └── pnl_vs_sentiment.png
└── README.md

## How to Run

python notebook/analysis.py

## Conclusion

Market sentiment significantly impacts trader performance and behavior.
Using sentiment-aware risk management can improve trading outcomes.
