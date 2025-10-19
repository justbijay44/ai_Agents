import yfinance as yf
from crewai.tools import tool

@tool("RealTime Stock Info Tool")
def get_stock_price(stock_symbol: str) -> str:
    """
    Retrieve the latest stock price and relvant information around the given symbol with the help of yfinance.

    Parameter: 
    - stock_symbol represents the symbol of a company like AAPL for the Apple Company

    Returns:
    - a relavant info around the stock_symbol like current price, daily changes.
    """

    stock = yf.Ticker(stock_symbol)
    info = stock.info

    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency", "USD")

    if current_price is None:
        return f"Couldn't find any relavant information around {stock_symbol}. Please Check the symbol."
    
    return (
        f"Stock: {stock_symbol.upper()}\n"
        f"Current Price: {current_price}\n"
        f"Price Change: {change} ({round(change_percent, 2)}%)\n"
    )

# print(get_stock_price('AAPL'))
