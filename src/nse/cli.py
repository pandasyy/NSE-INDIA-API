#!/usr/bin/env python3
"""CLI tool for NSE API"""
import argparse
import json
from datetime import datetime
from pathlib import Path
from nse import NSE

def main():
    parser = argparse.ArgumentParser(description="NSE India API CLI")
    parser.add_argument("--dir", default=".", help="Download directory")
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Quote command
    quote_parser = subparsers.add_parser("quote", help="Get stock quote")
    quote_parser.add_argument("symbol", help="Stock symbol")
    
    # Status command
    subparsers.add_parser("status", help="Market status")
    
    # Gainers command
    gainers_parser = subparsers.add_parser("gainers", help="Top gainers")
    gainers_parser.add_argument("--index", default="NIFTY 50", help="Index name")
    gainers_parser.add_argument("--count", type=int, default=10, help="Number of results")
    
    # Losers command
    losers_parser = subparsers.add_parser("losers", help="Top losers")
    losers_parser.add_argument("--index", default="NIFTY 50", help="Index name")
    losers_parser.add_argument("--count", type=int, default=10, help="Number of results")
    
    # Bhavcopy command
    bhav_parser = subparsers.add_parser("bhavcopy", help="Download bhavcopy")
    bhav_parser.add_argument("--date", help="Date (YYYY-MM-DD)", default=datetime.now().strftime("%Y-%m-%d"))
    bhav_parser.add_argument("--type", choices=["equity", "fno", "delivery"], default="equity")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
        
    with NSE(args.dir) as nse:
        if args.command == "quote":
            data = nse.equityQuote(args.symbol)
            print(json.dumps(data, indent=2))
            
        elif args.command == "status":
            data = nse.status()
            print(json.dumps(data, indent=2))
            
        elif args.command == "gainers":
            data = nse.listEquityStocksByIndex(args.index)
            gainers = nse.gainers(data, args.count)
            print(json.dumps(gainers, indent=2))
            
        elif args.command == "losers":
            data = nse.listEquityStocksByIndex(args.index)
            losers = nse.losers(data, args.count)
            print(json.dumps(losers, indent=2))
            
        elif args.command == "bhavcopy":
            dt = datetime.strptime(args.date, "%Y-%m-%d")
            if args.type == "equity":
                file = nse.equityBhavcopy(dt)
            elif args.type == "fno":
                file = nse.fnoBhavcopy(dt)
            else:
                file = nse.deliveryBhavcopy(dt)
            print(f"Downloaded: {file}")

if __name__ == "__main__":
    main()
