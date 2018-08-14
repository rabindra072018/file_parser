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


def get_bullet(input_string=[]):
    tree = []
    root = Node()
    root.children = tree

    tokens = input_string  # ["*", "*", "*", "*", "**", "**", "***", "***", "***", "**", "***", "***", "*"]
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
    return last_node

def print_tree(node=Node):
    next_node = node
    out_str = ""
    while next_node is not None:
        out_str += str(next_node.data)
        next_node = next_node.parent
        if next_node is not None and next_node.parent is not None:
            out_str += "."
    print(out_str)


def climb_to_sibling(node=Node, dest_token=None):
    next_node = node
    out_str = ""
    while next_node is not None:
        if next_node.token == dest_token:
            return next_node
        next_node = next_node.parent
