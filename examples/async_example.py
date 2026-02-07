"""Example: Fetch multiple quotes concurrently"""
import asyncio
from nse.async_nse import AsyncNSE

async def main():
    symbols = ["HDFCBANK", "INFY", "TCS", "RELIANCE", "WIPRO"]
    
    async with AsyncNSE("./data") as nse:
        print(f"Fetching quotes for {len(symbols)} symbols...")
        quotes = await nse.fetch_multiple_quotes(symbols)
        
        for symbol, quote in quotes.items():
            print(f"{symbol}: {quote.get('priceInfo', {}).get('lastPrice', 'N/A')}")

if __name__ == "__main__":
    asyncio.run(main())
