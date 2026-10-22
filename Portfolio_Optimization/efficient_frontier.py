import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assets
tickers = ["VOO", "VTI", "QQQ"]

# Download historical data
prices = yf.download(tickers, period="1y")["Close"]

# Daily returns
returns = prices.pct_change().dropna()

# Storage
portfolio_returns = []
portfolio_volatilities = []
portfolio_sharpes = []
portfolio_weights = []

risk_free_rate = 0.04

# Generate random portfolios
for _ in range(5000):

    weights = np.random.random(len(tickers))
    weights /= np.sum(weights)

    annual_return = np.sum(returns.mean() * weights) * 252

    covariance_matrix = returns.cov() * 252

    annual_volatility = np.sqrt(
        np.dot(
            weights.T, np.dot(covariance_matrix, weights)
        )
    )

    sharpe_ratio = (
        annual_return - risk_free_rate) / annual_volatility
    
    portfolio_returns.append(annual_return)
    portfolio_volatilities.append(annual_volatility)
    portfolio_sharpes.append(sharpe_ratio)
    portfolio_weights.append(weights)

# Find best Sharpe portfolio
best_index = np.argmax(portfolio_sharpes)

best_return = portfolio_returns[best_index]
best_volatility = portfolio_volatilities[best_index]
best_sharpe= portfolio_volatilities[best_index]
best_weights = portfolio_weights[best_index]

#Print results
print("\nOptimal Portfolio")

for ticker, weight in zip(tickers, best_weights):
    print(f"{ticker}: {weight:.2%}")

print(f"\nExpected Return: {best_return:.2%}")
print(f"Expected Volatility: {best_volatility:.2%}")
print(f"Best Sharpe Ratio: {best_sharpe:.2f}")


# Plot Efficient Frontier
plt.figure(figsize=(12, 7))

scatter = plt.scatter(
    portfolio_volatilities,
    portfolio_returns,
    c=portfolio_sharpes,
    cmap="viridis",
    alpha=0.7
)

# Highlight optimal portfolio
plt.scatter(
    best_volatility,
    best_return,
    color="red",
    marker="*",
    s=500,
    label="Max Sharpe Portfolio"
)

plt.colorbar(scatter, label="Sharpe Ratio")

plt.title("Efficient Frontier")
plt.xlabel("Annualized Volatility")
plt.ylabel("Annualized Return")

plt.legend()
plt.grid(True)

plt.show()