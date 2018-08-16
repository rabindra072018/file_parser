import re


class Token:
    def __init__(self, token=None, tok_type=None):
        self.token = token
        self.tok_type = tok_type
        self.expandable = False


class SequenceGenerator:
    token_list = []
    texts_list = []
    __sequence_curr_char = 0
    __number_list = []
    input_text = ""
    curr_index = 0

    bullets = []
    bullet_numbers = []

    def __init__(self, text):
        self.input_text = text
        self.curr_index = 0
        self.token_list = list()
        self.texts_list = list()

    def parse(self):

        while self.curr_index < len(self.input_text):
            symbol = self.input_text[self.curr_index]
            if symbol == "*":
                self.stars_collector()
            elif symbol == ".":
                self.dots_collector()
            else:
                self.texts_collector()

    def stars_collector(self):
        stars = ""
        while self.curr_index < len(self.input_text) and self.input_text[self.curr_index] == "*":
            stars = stars + self.input_text[self.curr_index]
            self.curr_index += 1
        token_object = Token(token=stars, tok_type="stars")
        self.token_list.append(token_object)

    def dots_collector(self):
        dots = ""
        while self.curr_index < len(self.input_text) and self.input_text[self.curr_index] == ".":
            dots = dots + self.input_text[self.curr_index]
            self.curr_index += 1
        token_object = Token(token=dots, tok_type="dots")
        self.token_list.append(token_object)

    def texts_collector(self):
        texts = ""
        while self.curr_index < len(self.input_text) and \
                self.input_text[self.curr_index] != "*" and \
                self.input_text[self.curr_index] != ".":
            texts = texts + self.input_text[self.curr_index]
            self.curr_index += 1

        texts = texts.lstrip()
        text_string = self.line_spliter(texts)
        for item in text_string:
            token_object = Token(token=item, tok_type="text")
            self.token_list.append(token_object)

    def line_spliter(self, lines=None):
        line_list = []
        temp_line = ""
        for index in range(len(lines)):
            if lines[index] == '\n':
                temp_line += "\n"
                line_list.append(temp_line)
                temp_line = ""
                continue
            temp_line += lines[index]
        line_list = list(filter(lambda x: x != "\n", line_list))
        return line_list
