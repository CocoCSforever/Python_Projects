import re


class TextCleaner:
    """Carry out the text pre-processing"""
    def __init__(self, filename):
        self.file_name = filename

    def process(self, file_text):
        # delete punctuation excluding '.' and '''
        file_text = re.sub(r'[^\w\s\'\.,]', '', file_text)

        # delete '.' at the end of abbreviated like "Mr." and "Dr."
        file_text = re.sub(r'([A-Z]([a-z]+)?)\.', r'\1', file_text)

        # change string to lowercase
        file_text = file_text.lower()

        # replace ',' with COMMA
        file_text = file_text.replace(',', ' COMMA')
        return file_text

    def read_file(self):
        try:
            f = open(self.file_name, "r", encoding="utf-8")
        except FileNotFoundError as e:
            print("Can't open", self.file_name)
            return
        # read file as a whole string
        file_text = f.read()
        return self.process(file_text)
