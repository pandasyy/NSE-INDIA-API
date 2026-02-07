"""Example: Using cache to reduce API calls"""
from pathlib import Path
from nse import NSE
from nse.cache import SimpleCache

def main():
    cache = SimpleCache(Path("./data"), default_ttl=300)
    
    with NSE("./data") as nse:
        symbol = "HDFCBANK"
        
        # Try cache first
        quote = cache.get(f"quote_{symbol}")
        
        if quote:
            print(f"Cache hit for {symbol}")
        else:
            print(f"Cache miss for {symbol}, fetching from API...")
            quote = nse.equityQuote(symbol)
            cache.set(f"quote_{symbol}", quote, ttl=60)
        
        print(f"{symbol}: Open={quote['open']}, Close={quote['close']}")

if __name__ == "__main__":
    main()
