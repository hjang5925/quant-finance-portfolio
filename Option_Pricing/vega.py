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

# Vega
vega = (
    S * norm.pdf(d1) * np.sqrt(T)
)

print(f"Call Vega:{vega:.4f}")