import numpy as np

# Inputs
S = 100
K = 105
T = 1
r = 0.04
sigma = 0.20

# Simulation settings
num_simulations = 100000

# Generate random stock prices at expiration
Z = np.random.standard_normal(num_simulations)

ST = S * np. exp(
    (r - 0.5 * sigma**2) * T
    + sigma * np.sqrt(T) * Z
)

# Call option payoff
payoffs = np.maximum(ST - K, 0)

# Discount payoff back to present value
call_price = np.exp(-r * T) * np.mean(payoffs)

print(f"Monte Carlo Call Price: {call_price:.2f}")