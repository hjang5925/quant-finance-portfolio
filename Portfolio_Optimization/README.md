# Portfolio Optimization

## Overview

This project applies Modern Portfolio Theory (MPT) to construct and evaluate ETF portfolios using historical market data.

The objective is to identify portfolio allocations that provide the highest risk-adjusted return.

---

## Assets

- VOO (Vanguard S&P 500 ETF)
- VTI (Vanguard Total Stock Market ETF)
- QQQ (Invesco NASDAQ-100 ETF)

---

## Features

- Historical ETF data retrieval
- Portfolio return calculation
- Portfolio volatility calculation
- Sharpe ratio optimization
- Random portfolio generation
- Efficient frontier visualization
- Maximum Sharpe portfolio identification

---

## Project Files

### portfolio_basics.py

Calculates:

- Expected Annual Return
- Expected Annual Volatility

for a user-defined ETF portfolio.

---

### portfolio_sharpe_search.py

Generates 1,000 random portfolios and identifies the portfolio with the highest Sharpe Ratio.

Outputs:

- Optimal Portfolio Weights
- Best Sharpe Ratio

---

### efficient_frontier.py

Generates 5,000 random portfolios and visualizes:

- Risk (Volatility)
- Return
- Sharpe Ratio
- Efficient Frontier

The portfolio with the highest Sharpe Ratio is highlighted on the chart.

---

## Example Results

Optimal Portfolio:

- VOO: 0.79%
- VTI: 83.56%
- QQQ: 15.65%

Metrics:

- Expected Return: 14.91%
- Expected Volatility: 12.84%
- Sharpe Ratio: 0.89

---

## Financial Concepts

This project demonstrates:

- Modern Portfolio Theory
- Risk vs Return Analysis
- Portfolio Diversification
- Sharpe Ratio Optimization
- Efficient Frontier Construction

---

## Future Improvements

- Minimum Variance Portfolio
- Portfolio Rebalancing
- Additional Asset Classes
- Multi-Year Backtesting

---

## Author

Hyejin Jang