import pandas as pd

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
    print(my_pipeline.df)