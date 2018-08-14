
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
        self.token_list.append(stars)

    def dots_collector(self):
        dots = ""
        while self.curr_index < len(self.input_text) and self.input_text[self.curr_index] == ".":
            dots = dots + self.input_text[self.curr_index]
            self.curr_index += 1
        self.token_list.append(dots)

    def texts_collector(self):
        texts = ""
        while self.curr_index < len(self.input_text) and \
                self.input_text[self.curr_index] != "*" and \
                self.input_text[self.curr_index] != ".":
            texts = texts + self.input_text[self.curr_index]
            self.curr_index += 1
        self.token_list.append(texts)