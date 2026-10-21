import yfinance as yf
import matplotlib.pyplot as plt

#ETFs to compare 
tickers = ["VOO", "VTI", "QQQ"]

# Download one year of price data
prices = yf.download(tickers, period="1y")["Close"]

# Normalize prices to start at 1.0
normalized = prices / prices.iloc[0]

# Create chart
normalized.plot(figsize=(10,6))

plt.title("ETF Performance Comparison")
plt.xlabel("Date")
plt.ylabel("Normalized Growth")
plt.grid(True)

plt.show()