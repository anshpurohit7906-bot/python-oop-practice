import pandas as pd
import matplotlib.pyplot as plt

class MarketPipeline :

    def __init__(self , file_path):
        self.df = pd.read_csv(file_path)

    def calculate_average_price(self ):
        return self.df["Price"].mean()
    
    def get_highest_price(self):
        return self.df["Price"].max()
    
    def total_volume(self):
        return self.df["Volume"].sum()

    def get_lowest_price(self):
        return self.df["Price"].min()
    
    def generate_summary_report(self):
        avg_price = self.calculate_average_price()
        max_price = self.get_highest_price()
        min_price = self.get_lowest_price()
        total_vol = self.total_volume()

        print(f"Average Price : {avg_price:,.2f}")
        print(f"Maximum Price : {max_price:,.2f}")
        print(f"Minimum Price : {min_price:,.2f}")
        print(f"Total_volume  : {total_vol:,}")
    
    def expensive_stocks(self , threshold):
        return self.df[self.df["Price"]> threshold]
    
    def plot_stock_prices(self):
        self.df.plot(x="Ticker", y="Price", kind="bar", color="skyblue", legend=False)

        plt.title("Real-Time Stock Price Comparison")
        plt.xlabel("Stock Ticker")
        plt.ylabel("Price ($)")

        plt.tight_layout()
        plt.show()

    def plot_volume_chart(self):
        self.df.plot(x = "Ticker", y = "Volume" , kind = "bar")

        plt.title("Real Time Stock Volume Comparison")
        plt.xlabel("Stock Ticker")
        plt.ylabel("Volume")

        plt.tight_layout()
        plt.show()

    def plot_price_trend(self,ticker_symbol):

        filtered_df = self.calculate_moving_average(ticker_symbol)

        plt.plot(filtered_df["Date"],filtered_df["Price"],marker = "o",color = "green",label="Daily Price")
        plt.plot(filtered_df["Date"],filtered_df["MA_3"],linestyle = "--",color = "red",label="3-Day Moving Average")

        plt.title(f"{ticker_symbol} Price Trend & Moving Average")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.tight_layout()
        plt.xticks(rotation = 45)
        plt.show()

    def calculate_moving_average(self,ticker_symbol):
       filtered_df = self.df[self.df["Ticker"] == ticker_symbol].copy()
       filtered_df["MA_3"] = filtered_df["Price"].rolling(window=3).mean().bfill()
       return filtered_df
    
