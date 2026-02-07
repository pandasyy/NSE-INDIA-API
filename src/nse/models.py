"""Data models using dataclasses"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Quote:
    """Stock quote data model"""
    symbol: str
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    
@dataclass
class MarketStatus:
    """Market status data model"""
    market: str
    status: str
    
@dataclass
class OptionData:
    """Option chain data"""
    strike: float
    call_oi: int
    put_oi: int
    call_ltp: float
    put_ltp: float
    pcr: Optional[float] = None
