import yfinance as yf
import pandas as pd
import os


def fetch_stock_data(ticker="HDFCBANK.NS", period="1y", interval="1d", save_csv=True):
    """
    Fetch historical stock data using yfinance

    :param ticker: str: Stock symbol (use .NS for NSE India)
    :param period: str: Timme range (e.g., '1y', '6mo', '5d')
    :param interval: str: Data frequency ('1d', '1wk, '1mo')
    :param save_csv: bool: Whether to save the data as a csv file
    :return: pd.DataFrame: Stock historical data
    """
    print(f"Fetching historical data for {ticker} over period {period} with interval {interval} interval...")

    try:
        df = yf.download(tickers=ticker, period=period, interval=interval, progress=False)
        if df.empty:
            raise ValueError("No data fetched. Please check the ticker or the network")

        df.reset_index(inplace=True)

        if save_csv:
            output_dir = "data/raw"
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, f"{ticker.replace('.', '_')}_{period}_{interval}.csv")
            df.to_csv(filepath, index=False)
            print(f"Data saved to {filepath}")

        return df

    except Exception as e:
        print(f"⚠️ Error fetching data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error


if __name__ == "__main__":
    stocks = ["HDFCBANK.NS", "INFY.NS", "RELIANCE.NS"]
    for stock in stocks:
        fetch_stock_data(stock, period="1y", interval="1d")
