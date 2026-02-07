"""Custom exceptions for better error handling"""

class NSEException(Exception):
    """Base exception for NSE API"""
    pass

class NSETimeoutError(NSEException):
    """Request timeout"""
    pass

class NSEConnectionError(NSEException):
    """Connection failed"""
    pass

class NSEDataNotAvailable(NSEException):
    """Data not available for requested parameters"""
    pass

class NSEInvalidSymbol(NSEException):
    """Invalid stock symbol"""
    pass

class NSERateLimitError(NSEException):
    """Rate limit exceeded"""
    pass

class NSEAuthError(NSEException):
    """Authentication/Cookie error"""
    pass
