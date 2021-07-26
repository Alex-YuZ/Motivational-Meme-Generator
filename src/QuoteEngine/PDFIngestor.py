"""This module is for parsing .pdf file and returning the quotes extracted."""
from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """Inheriting class from IngestorInterface"""
    
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse and extract data from .pdf file

        Args:
            path (str): file path where the .pdf file lives

        Returns:
            List[QuoteModel]: a list consisting of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception('file format inconsistency error!')
        
        tmp_txt = "./{}.txt".format(random.sample(range(10000), 1))
        call = subprocess.call(['pdftotext', '-layout', path, tmp_txt])
        
        try:
            quotes = []
            with open(tmp_txt, 'r') as infile:
                for line in infile.readlines():
                    line = line.strip('\n\r').strip()
                    if len(line) > 0:
                        line = line.split(' - ')
                        quotes.append(QuoteModel(line[0], line[1]))
            os.remove(tmp_txt)
        
        except Exception as e:
            print("File parse failed!")
        
        return quotes