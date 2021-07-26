"""This module is for parsing .docx file and returning the quotes extracted."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx

class DocxIngestor(IngestorInterface):
    """Inheriting class from IngestorInterface"""
    
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse and extract data from .docx file

        Args:
            path (str): file path where the .docx file lives

        Returns:
            List[QuoteModel]: a list consisting of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception('file format inconsistency error!')
        
        try: 
            doc = docx.Document(path)
            quotes = []
            for p in doc.paragraphs:
                if len(p.text) > 0:
                    line = p.text.strip('\n').strip().split(' - ')
                    quotes.append(QuoteModel(line[0], line[1]))
        
        except Exception as e:
            print("File parse failed!")
                
        return quotes