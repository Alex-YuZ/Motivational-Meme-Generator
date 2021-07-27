"""This module is for parsing .pdf file and returning the quotes extracted."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Inheriting class from IngestorInterface"""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse and extract data from .txt file

        Args:
            path (str): file path where the .txt file lives

        Returns:
            List[QuoteModel]: a list consisting of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception('file format inconsistency error!')

        try:
            quotes = []
            with open(path, 'r') as infile:
                for line in infile.readlines():
                    line = line.strip('\n').strip()
                    if len(line) > 0:
                        line = line.split(' - ')
                        quotes.append(QuoteModel(line[0], line[1]))

        except Exception as e:
            print("File parse failed!")

        return quotes
