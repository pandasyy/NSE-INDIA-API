"""Tests for async NSE API"""
import pytest
import asyncio
from pathlib import Path
from nse.async_nse import AsyncNSE

@pytest.mark.asyncio
async def test_fetch_multiple_quotes():
    """Test concurrent quote fetching"""
    async with AsyncNSE("./test_data") as nse:
        symbols = ["HDFCBANK", "INFY", "TCS"]
        results = await nse.fetch_multiple_quotes(symbols)
        assert len(results) > 0
        
@pytest.mark.asyncio
async def test_context_manager():
    """Test async context manager"""
    async with AsyncNSE("./test_data") as nse:
        assert nse.client is not None
