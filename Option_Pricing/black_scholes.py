import numpy as np
from scipy.stats import norm

# Inputs
S = 100 # Stock Price
K = 105 # Strike Price
T = 1 # Time to Expiration (Years)
r = 0.04 # Risk-Free Rate
sigma = 0.2 # Volatility

# Black-Scholes calculations
d1 = (
    np.log(S/K)
    + (r + 0.5 * sigma**2) * T
) / (
    sigma * np.sqrt(T)
)

d2 = d1 - sigma * np.sqrt(T)

call_price = (
    S * norm.cdf(d1)
    - K * np.exp(-r * T) * norm.cdf(d2)
)

print(f"Call Option Price: ${call_price:.2f}")