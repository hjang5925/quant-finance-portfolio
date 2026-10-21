import yfinance as yf

tickers = ["VOO", "VTI", "QQQ"]

for ticker in tickers:
    data = yf.download(ticker, period="1y")

    close_prices = data["Close"][ticker]

    start_price = close_prices.iloc[0]
    end_price = close_prices.iloc[-1]

    total_return = (end_price / start_price - 1) * 100

    print(f"{ticker}: {total_return: .2f}%")