import yfinance as yf
import pandas as pd
import numpy as np

# Portfolio assets
tickers = ["VOO", "VTI", "QQQ"]

# Portfolio weights
weights = np.array([0.4, 0.3, 0.3])

# Download historical prices
prices = yf.download(tickers, period="1y")["Close"]

# Daily returns
returns = prices.pct_change().dropna()

# Portfolio daily returns
portfolio_returns = returns.dot(weights)

# Annual return
annual_return = portfolio_returns.mean() * 252

# Annual volatility
annual_volatility = portfolio_returns.std() * np.sqrt(252)

risk_free_rate = 0.04

# Add Sharpe Ratio
sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility

print(f"Expected Annual Return: {annual_return:.2%}")
print(f"Expected Annual Volatility: {annual_volatility:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")