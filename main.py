import sys
from financial_pipeline import MarketPipeline


if __name__ == "__main__":

    try: 
        my_pipeline = MarketPipeline("market_data.csv")
    except FileNotFoundError:
        print("Error! File not found")
        sys.exit(1)
        
    my_pipeline.generate_summary_report()
        
    print ("Generating Stock Price Chart...")
    my_pipeline.plot_stock_prices()
    print ("Generating Stock Volume Chart...")
    my_pipeline.plot_volume_chart()
   
    target_ticker = "NVDA"
    if target_ticker not in my_pipeline.df["Ticker"].values:
        print("Error: Ticker 'NVDA' was not found in the dataset.")
    else:
        print("Generating Trend and Moving Average Chart...")
        my_pipeline.plot_price_trend(target_ticker)