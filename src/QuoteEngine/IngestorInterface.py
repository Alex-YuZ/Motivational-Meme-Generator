"""Abstrac Base Class for file ingestors."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """abstract base class for file ingestors."""
    
    allowed_extensions = []
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Verify file format consistency

        Args:
            path (str): file path where the file lives

        Returns:
            bool: True if the file extension is consistent
                    with the allowed_extions
        """
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """abstract method to be realized in its inheritance classes."""
        pass