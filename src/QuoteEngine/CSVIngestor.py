"""This module is for parsing .csv file and returning the quotes extracted."""
from typing import List
import pandas as pd
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Inheriting class from IngestorInterface"""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse and extract data from .csv file

        Args:
            path (str): file path where the .csv file lives

        Returns:
            List[QuoteModel]: a list consisting of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception('file format inconsistency error!')

        try:
            df = pd.read_csv(path, header=0)
            quotes = []
            for _, row in df.iterrows():
                quotes.append(QuoteModel(row["body"], row["author"]))

        except Exception as e:
            print("File parse failed!")

        return quotes
