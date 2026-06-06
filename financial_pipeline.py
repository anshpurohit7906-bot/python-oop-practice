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

    def plot_price_trend(self):

        self.calculate_moving_average()

        plt.plot(self.df["Date"],self.df["Price"],marker="o",color="green",label="Daily Price")

        plt.plot(self.df["Date"],self.df["MA_3"],linestyle="--",color="red",label="3-day moving avg")


        plt.title("NVDA 7-Day Price Trend")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.grid(True)
        plt.legend()

        plt.tight_layout()
        plt.xticks(rotation = 45)
        plt.show()

    def calculate_moving_average(self):
        self.df["MA_3"] = self.df["Price"].rolling(window=3).mean()

if __name__ == "__main__":

    my_pipeline = MarketPipeline("market_data.csv")
    avg = my_pipeline.calculate_average_price()
    high = my_pipeline.get_highest_price()
    vol = my_pipeline.total_volume()
    low = my_pipeline.get_lowest_price()
    exp = my_pipeline.expensive_stocks(200)
    print(avg)
    print(high)
    print(vol)
    print(low)    
    print(exp)
    print ("Generating Stock Price Chart...")
    my_pipeline.plot_stock_prices()
    print ("Generating Stock Volume Chart...")
    my_pipeline.plot_volume_chart()
    print("Generating Historical Trend Line...")
    my_pipeline.plot_price_trend()
    print("Generating Trend and Moving Average Chart...")
    my_pipeline.plot_price_trend()