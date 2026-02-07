"""Caching layer for NSE API responses"""
import json
import time
from pathlib import Path
from typing import Any, Optional

class SimpleCache:
    """Simple file-based cache with TTL"""
    
    def __init__(self, cache_dir: Path, default_ttl: int = 300):
        self.cache_dir = cache_dir / ".cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.default_ttl = default_ttl
        
    def get(self, key: str) -> Optional[Any]:
        """Get cached value if not expired"""
        cache_file = self.cache_dir / f"{key}.json"
        if not cache_file.exists():
            return None
            
        try:
            data = json.loads(cache_file.read_text())
            if time.time() - data["timestamp"] < data["ttl"]:
                return data["value"]
        except:
            pass
        return None
        
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """Cache value with TTL"""
        cache_file = self.cache_dir / f"{key}.json"
        data = {
            "value": value,
            "timestamp": time.time(),
            "ttl": ttl or self.default_ttl
        }
        cache_file.write_text(json.dumps(data))
        
    def clear(self):
        """Clear all cache"""
        for f in self.cache_dir.glob("*.json"):
            f.unlink()
