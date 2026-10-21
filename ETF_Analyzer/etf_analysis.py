import yfinance as yf

# Downdload one month of VOO price data
voo = yf.download("VOO", period="1mo")

# Basic dataset information
print("\nDataset Shape:")
print(voo.shape)

print("\nColumns:")
print(voo.columns)

print("\nLatest Trading Day:")
print(voo.tail(1))