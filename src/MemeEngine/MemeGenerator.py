"""
This module is used for making the meme:
1. Load the image
2. Resize the image
3. Overlay words on the image
"""
from PIL import Image, ImageDraw, ImageFont
import random
from QuoteEngine.QuoteModel import QuoteModel


class MemeEngine():
    def __init__(self, output_dir):
        """Initialize with output directory"""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """class method for meme generation

        Args:
            img_path (str): where the images live
            text (str): quote body to be added on the image
            author (str): quote author to be added on the image
            width (int, optional): Adjust image width. Defaults to 500.

        Returns:
            str: path to the generated meme
        """

        # load the image
        img = Image.open(img_path)

        # get properties of the image
        ori_width, ori_height = img.size

        # Verify validity of width assignment
        if width > 500:
            width = 500

        # original aspect ratio of height/width
        aspect_ratio = ori_height/ori_width

        # Resize image while keeping original aspect ratio
        new_height = int(width*aspect_ratio)
        img = img.resize((width, new_height), Image.NEAREST)

        # Add message on image
        msg = repr(QuoteModel(text, author))
        random_width = random.randint(0, int(width/4))
        random_height = random.randint(0, int(new_height/2))
        draw = ImageDraw.Draw(img)
        font_file = "./MemeEngine/LilitaOne-Regular.ttf"
        font = ImageFont.truetype(font_file, size=20)
        draw.text((random_width, random_height),
                  msg,
                  font=font,
                  fill='yellow')

        # string for the file name (directory) of the generated meme
        file_path = "{}/{}.png".format(self.output_dir,
                                       random.randint(0, 1000))

        # Save
        img.save(file_path)

        return file_path
