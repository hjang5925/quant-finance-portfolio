import numpy as np
from scipy.stats import norm

# Inputs
S = 100 # Stock Price
K = 105 # Strike Price
T = 1 # Time to Expiration (Years)
r = 0.04 # Risk-Free Rate
sigma = 0.2 # Volatility

# Black-Scholes d1
d1 = (
    np.log(S/K)
    + (r + 0.5 * sigma**2) * T
) / (
    sigma * np.sqrt(T)
)

# Call Delta
delta = norm.cdf(d1)

print(f"Call Delta: {delta:.4f}")