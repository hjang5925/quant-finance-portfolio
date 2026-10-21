import yfinance as yf
import numpy as np

tickers = {"VOO", "VTI", "QQQ"}

for ticker in tickers:
    data = yf.download(ticker, period="1y")

    close_prices = data["Close"][ticker]

    daily_returns = close_prices.pct_change().dropna()

    volatility = daily_returns.std() * np.sqrt(252) * 100

    print(f"{ticker}: {volatility:.2f}% annualized volatility")