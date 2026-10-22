import yfinance as yf
import pandas as pd
import numpy as np

tickers = ["VOO", "VTI", "QQQ"]

prices = yf.download(tickers, period="1y")["Close"]

returns = prices.pct_change().dropna()

best_sharpe = -999
best_weights = None

risk_free_rate = 0.04

# Generate 1,000 random portfolios
for _ in range(1000):

    # Create random portfolio weights
    weights = np.random.random(3)
    weights = weights / np.sum(weights)

    # Calculate portfolio daily returns
    portfolio_returns = returns.dot(weights)

    # Calculate annualized metrics
    annual_return = portfolio_returns.mean() * 252
    annual_volatility = portfolio_returns.std() * np.sqrt(252)

    # Calculate Sharpe Ratio
    sharpe = (
        annual_return - risk_free_rate) / annual_volatility

    if sharpe > best_sharpe:
        best_sharpe = sharpe
        best_weights = weights
print("\nOptimal Portfolio Weights")

for ticker, weight in zip(tickers, best_weights):
    print(f"{ticker}: {weight:.2%}")

print(f"\nBest Sharpe Ratio: {best_sharpe: .2f}")
