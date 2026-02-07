"""Data export utilities"""
import csv
import json
from pathlib import Path
from typing import List, Dict, Any

class DataExporter:
    """Export data to various formats"""
    
    @staticmethod
    def to_csv(data: List[Dict[str, Any]], filepath: Path):
        """Export to CSV"""
        if not data:
            return
        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            
    @staticmethod
    def to_json(data: Any, filepath: Path, indent: int = 2):
        """Export to JSON"""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=indent)
            
    @staticmethod
    def to_parquet(data: List[Dict[str, Any]], filepath: Path):
        """Export to Parquet (requires pandas/pyarrow)"""
        try:
            import pandas as pd
            df = pd.DataFrame(data)
            df.to_parquet(filepath, index=False)
        except ImportError:
            raise ImportError("pandas and pyarrow required for parquet export")
