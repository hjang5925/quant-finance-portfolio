import yfinance as yf
import numpy as np

tickers = ["VOO", "VTI", "QQQ"]

risk_free_rate = 0.04

for ticker in tickers:
    data = yf.download(ticker, period="1y")

    close_prices = data["Close"][ticker]

    daily_returns = close_prices.pct_change().dropna()

    annual_return = (close_prices.iloc[-1] / close_prices.iloc[0] -1)

    annual_volatility = daily_returns.std() * np.sqrt(252)

    sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility

    print(
        f"{ticker}: "
        f"Return={annual_return:.2%}, "
        f"Volatility={annual_volatility:.2%}, "
        f"Sharpe={sharpe_ratio:.2f}"
        )