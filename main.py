from financial_pipeline import MarketPipeline


if __name__ == "__main__":

    my_pipeline = MarketPipeline("market_data.csv")
    
    my_pipeline.generate_summary_report()
    
    print ("Generating Stock Price Chart...")
    my_pipeline.plot_stock_prices()
    print ("Generating Stock Volume Chart...")
    my_pipeline.plot_volume_chart()
    print("Generating Trend and Moving Average Chart...")
    my_pipeline.plot_price_trend("NVDA")