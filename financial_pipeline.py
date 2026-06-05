import pandas as pd

# Raw incoming financial data stream
raw_market_stream = {
    "Ticker": ["AAPL", "TSLA", "NVDA", "MSFT", "AMD"],
    "Price": [175.50, 180.25, 875.00, 420.30, 170.10],
    "Volume": [52000000, 85000000, 41000000, 23000000, 48000000]
}

df = pd.DataFrame(raw_market_stream)
#print(df)

average_price = df["Price"].mean()
#print(average_price)


class MarketPipeline :

    def __init__(self , data_stream):
        self.df = pd.DataFrame(data_stream)

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

my_pipeline = MarketPipeline(raw_market_stream)
avg = my_pipeline.calculate_average_price()
max = my_pipeline.get_highest_price()
vol = my_pipeline.total_volume()
min = my_pipeline.get_lowest_price()
exp = my_pipeline.expensive_stocks(200)
print(avg)
print(max)
print(vol)
print(min)    
print(exp)