"""Module for Web service construction using Flask"""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeEngine.MemeGenerator import MemeEngine

app = Flask(__name__)

# create a directory to store the generated meme images
if not os.path.isdir('./static'):
    output_str = ("output folder {} has been created"
                  "in the working directory!")
    print(output_str.format("static"))
    os.mkdir('./static')
else:
    pass

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # select a random image from imgs array
    img = random.choice(imgs)

    # select a random quote from the quotes array
    quote = random.choice(quotes)

    # make the meme and return its output directory
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    path = None
    img_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    # Use requests to save the image from the image_url
    # form param to a temp local file.
    response = requests.get(img_url, allow_redirects=True)
    tmp = "./static/{}.png".format(random.randint(0, 10000))
    with open(tmp, 'wb') as infile:
        infile.write(response.content)

    # Use the meme object to generate a meme using this temp
    # file and the body and author form paramaters.
    path = meme.make_meme(tmp, body, author)

    # Remove the temporary saved image.
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
