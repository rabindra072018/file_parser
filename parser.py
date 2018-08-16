from SequenceGenerator import *
from bullet_generator import *
import sys


def get_dot_alignment(token=Token):
    alignment_count = len(token.token)
    alignment_symbol = "-"
    if token.expandable:
        alignment_symbol = "+"
    final_string = " " * alignment_count + alignment_symbol
    return final_string


def create_line_shrink(token_list=[]):
    for index in range(len(token_list)):
        if token_list[index].tok_type == "dots" and index - 2 > -1:
            if token_list[index - 2].tok_type == "dots":
                if len(token_list[index - 2].token) < len(token_list[index].token):
                    token_list[index - 2].expandable = True


def main(text=None):
    # l = ["*", "*", ".", "..", "...", "*", "**", "**", "***", "***", "***", "**", "*", "**", "**", "***"]

    # print(get_bullet(create_bullet(l)))

    # text = '* This is an outline ' \
    #        '. Its not a very good outline1' \
    #        '.. Its not a very good outline2' \
    #        '... Its not a very good outline3' \
    #        '* This is the second numbered item in the outline ' \
    #        '** Lots ' \
    #        '** Less Numbers' \
    #        '*** Level 3 Star' \
    #        '. Its not a very good outline50' \
    #        '. Its not a very good outline51' \
    #        '. Its not a very good outline52' \
    #        '*** Level 3 Star2' \
    #        '** Level 22'

    sq = SequenceGenerator(text=text)
    sq.parse()
    tokens = sq.token_list
    bullets = []
    text_line = ""
    align_ment = ""
    last_tok_type = ""
    final_string_list = []
    create_line_shrink(token_list=tokens)
    for token in tokens:
        if token.tok_type == "stars":
            bullets.append(token.token)
            last_tok_type = "stars"
            align_ment = ""
        elif token.tok_type == "dots":
            align_ment = get_dot_alignment(token=token)
            last_tok_type = "dots"
        elif token.tok_type == "text":
            if last_tok_type == "stars":
                bullet = get_bullet(create_bullet(bullets))
                text_line = bullet + " " + token.token
            elif last_tok_type == "dots":
                text_line = align_ment + token.token

            text_line = text_line.strip('\n')
            print(text_line)


def get_file_contents(file_name=None):
    out_str = ""
    file_data = open(file_name, "r").read()
    print(file_data)
    return out_str


def func_test():
    mylist = ["a1", "a2", "a3", "a4"]

    for index in range(0, len(mylist)):
        mylist[index] += " Modified"
        print(mylist[index])


if __name__ == '__main__':
    # out_str = ""
    # for data in sys.stdin:
    #     out_str += data
    # main(text=out_str)

    # Using file open
    main(text=open("t1.txt", "r").read())

    # func_test()
