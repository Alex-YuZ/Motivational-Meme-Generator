"""combination of all file ingestors"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """General class to parse files with all formats"""
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Combine different ingestors to parse different files

        Args:
            path (str): path where files live

        Returns:
            List[QuoteModel]: a list of QuoteModel objects
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)