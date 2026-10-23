import numpy as np
from scipy.stats import norm

# Inputs
S = 100
K = 105
T = 1
r = 0.04
sigma = 0.20

# d1
d1 = (
    np.log(S / K)
    + (r + 0.5 * sigma**2) * T
) / (
    sigma * np.sqrt(T)
)

d2 = d1 - sigma * np.sqrt(T)

# Call Theta
theta = (
    -(S * norm.pdf(d1) * sigma) /
     (2 * np.sqrt(T))
     - r * K * np.exp(-r * T) * norm.cdf(d2)
)

print(f"Call Theta: {theta:.4f}")