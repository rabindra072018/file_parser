class SequenceGenerator:
    token_list = []
    texts_list = []
    __sequence_curr_char = 0
    __number_list = []
    input_text = ""
    curr_index = 0

    bullets = []
    bullet_numbers = []

    # def add_bullets(self, bullet):
    #     self.bullets.append(bullet)
    #
    #
    # def print_bullets_number(self):
    #     for bullet in self.bullets:

    def __init__(self, text):
        self.input_text = text
        self.curr_index = 0

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


class Node:
    data = ""
    token = ""
    parent = None
    children = []

    def __init__(self):
        self.children = list()
        self.data = ""
        self.token = ""

    def get_parent(self):
        return self

    def set_parent(self, parent=None):
        self.parent = parent

    def set_data(self, data=None):
        self.data = data

    def add_child(self, parent=None, data=None):
        self.children.append(Node(parent=parent, data=data))

    def add_sibling(self, sibling=None):
        self.next = sibling
        sibling.previous = self


def print_tree(node=Node):
    next_node = node
    out_str = ""
    while next_node is not None:
        out_str += str(next_node.data)
        next_node = next_node.parent
        if next_node is not None and next_node.parent is not None:
            out_str += "."
    print(out_str)


def main():
    tree = []
    root = Node()
    root.children = tree

    tokens = ["*", "*", "*", "*", "**", "**", "***", "***", "***", "**", "***", "***", "*"]
    last_token = None
    last_node = None

    for curr_token in tokens:

        if len(tree) == 0:
            temp_node = Node()
            temp_node.token = curr_token
            temp_node.data = len(tree) + 1
            temp_node.parent = root
            tree.append(temp_node)
            last_node = temp_node
        elif len(curr_token) == len(last_token):
            temp_node = Node()
            temp_node.token = curr_token
            temp_node.data = len(last_node.parent.children) + 1
            temp_node.parent = last_node.parent
            last_node.parent.children.append(temp_node)
            last_node = temp_node
        elif len(curr_token) > len(last_token):
            temp_node = Node()
            temp_node.token = curr_token
            temp_node.data = len(last_node.children) + 1
            temp_node.parent = last_node
            last_node.children.append(temp_node)
            last_node = temp_node
        elif len(curr_token) < len(last_token):
            temp_node = Node()
            temp_node.token = curr_token
            sib_ling = climb_to_sibling(last_node, curr_token)
            temp_node.data = len(sib_ling.parent.children) + 1
            temp_node.parent = sib_ling.parent
            sib_ling.parent.children.append(temp_node)
            last_node = temp_node
        last_token = curr_token
    print_tree(last_node)


def climb_to_sibling(node=Node, dest_token=None):
    next_node = node
    out_str = ""
    while next_node is not None:
        if next_node.token == dest_token:
            print("found")
            return next_node
        next_node = next_node.parent

if __name__ == '__main__':
    main()
