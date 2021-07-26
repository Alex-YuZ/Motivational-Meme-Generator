"""Main program for execution on CLI"""
import os
import random
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeEngine.MemeGenerator import MemeEngine
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate a meme on a given image and quote 

    Args:
        path (str, optional): path to quotes files. Defaults to None.
        body (str, optional): body part of the quote. Defaults to None.
        author (str, optional): [author part of the quote. Defaults to None.

    Raises:
        Exception: [description]

    Returns:
        [type]: [description]
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)
        
    # check whether the output directory exists or not
    # if not, create one
    if not os.path.isdir('./tmp'):
        print("output folder {} has been created in the working directory!".format("tmp"))
        os.mkdir('./tmp')
    
    # do nothing if exists
    else:
        pass
    
    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    
    return path


if __name__ == "__main__":

    # parse CLI arguments
    parser = argparse.ArgumentParser(description='Meme Creation')
    parser.add_argument('--path', type=str, help='path to images to create from')
    parser.add_argument('--body', type=str, help='body text to overlay on the meme')
    parser.add_argument('--author', type=str, help='author text to overlay on the meme')
    args = parser.parse_args()
    
    # print out the location where the generated meme stores
    print(generate_meme(args.path, args.body, args.author))
