import yfinance as yf

# Download one year of VOO price data
voo = yf.download("VOO", period="1y")

# Extract close prices
close_prices = voo["Close"]["VOO"]

# Get first and last price
start_price = close_prices.iloc[0]
end_price = close_prices.iloc[-1]

# Calculate total return
total_return = (end_price / start_price - 1)* 100 

print(f"Starting Price: ${start_price:.2f}")
print(f"Ending Price: ${end_price:.2f}")
print(f"Total Return: ${total_return:.2f}%")
