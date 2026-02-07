"""Tests for caching"""
import pytest
from pathlib import Path
from nse.cache import SimpleCache

def test_cache_set_get(tmp_path):
    """Test cache set and get"""
    cache = SimpleCache(tmp_path)
    cache.set("test_key", {"data": "value"})
    result = cache.get("test_key")
    assert result == {"data": "value"}
    
def test_cache_expiry(tmp_path):
    """Test cache expiry"""
    cache = SimpleCache(tmp_path, default_ttl=1)
    cache.set("test_key", {"data": "value"}, ttl=0)
    result = cache.get("test_key")
    assert result is None
