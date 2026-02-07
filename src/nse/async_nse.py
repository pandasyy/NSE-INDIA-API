"""Async NSE API with concurrent request support"""
import asyncio
import json
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List, Optional, Union
import httpx

class AsyncNSE:
    """Async version of NSE API for concurrent requests"""
    
    def __init__(self, download_folder: Union[str, Path], timeout: int = 15):
        self.dir = Path(download_folder) if isinstance(download_folder, str) else download_folder
        self.dir.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout
        self.base_url = "https://www.nseindia.com/api"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/118.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
        }
        
    async def __aenter__(self):
        self.client = httpx.AsyncClient(http2=True, headers=self.headers, timeout=self.timeout)
        return self
        
    async def __aexit__(self, *args):
        await self.client.aclose()
        
    async def fetch_multiple_quotes(self, symbols: List[str]) -> Dict[str, Dict]:
        """Fetch quotes for multiple symbols concurrently"""
        tasks = [self._get_quote(symbol) for symbol in symbols]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {sym: res for sym, res in zip(symbols, results) if not isinstance(res, Exception)}
        
    async def _get_quote(self, symbol: str) -> Dict:
        """Internal method to get single quote"""
        url = f"{self.base_url}/quote-equity"
        response = await self.client.get(url, params={"symbol": symbol.upper()})
        return response.json()
