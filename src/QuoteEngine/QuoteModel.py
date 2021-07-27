"""This modeul intendes to create QuoteModel object

When referred to, a QuoteModel object will print out
as: "{body part} - {author part}"
"""


class QuoteModel():
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        return """"{}" - {}""".format(self.body, self.author)
