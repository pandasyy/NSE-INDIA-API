"""Example: Export data to various formats"""
from pathlib import Path
from nse import NSE
from nse.export import DataExporter

def main():
    with NSE("./data") as nse:
        # Get NIFTY 50 stocks
        data = nse.listEquityStocksByIndex("NIFTY 50")
        stocks = data["data"]
        
        # Export to CSV
        DataExporter.to_csv(stocks, Path("nifty50.csv"))
        print("Exported to nifty50.csv")
        
        # Export to JSON
        DataExporter.to_json(stocks, Path("nifty50.json"))
        print("Exported to nifty50.json")
        
        # Export to Parquet (requires pandas)
        try:
            DataExporter.to_parquet(stocks, Path("nifty50.parquet"))
            print("Exported to nifty50.parquet")
        except ImportError:
            print("Install pandas and pyarrow for parquet export")

if __name__ == "__main__":
    main()
