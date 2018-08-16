from SequenceGenerator import *
from bullet_generator import *
import sys


def get_alignment_symbol_and_space(token=Token):
    alignment_symbol = "-"
    if token.expandable:
        alignment_symbol = "+"
    return alignment_symbol, " " * len(token.token)


def create_line_shrink(token_list=[]):
    for index in range(len(token_list)):
        if token_list[index].tok_type == Token.DOTS and index - 2 > -1:
            if token_list[index - 2].tok_type == Token.DOTS:
                if len(token_list[index - 2].token) < len(token_list[index].token):
                    token_list[index - 2].expandable = True


def main(text=None):
    sq = SequenceGenerator(text=text)
    sq.parse()
    tokens = sq.token_list
    bullets = []
    text_line = ""
    alignment_space = ""
    last_tok_type = ""
    create_line_shrink(token_list=tokens)
    for token in tokens:
        if token.tok_type == Token.STARS:
            bullets.append(token.token)
            last_tok_type = Token.STARS
            alignment_space = ""
        elif token.tok_type == Token.DOTS:
            alignment_space = get_alignment_symbol_and_space(token=token)
            last_tok_type = token.tok_type
        elif token.tok_type == Token.TEXTS:
            if last_tok_type == Token.STARS:
                bullet = get_bullet(create_bullet(bullets))
                text_line = bullet + " " + token.token
            elif last_tok_type == Token.DOTS:
                text_line = alignment_space[1] + alignment_space[0] + " " + token.token
            elif last_tok_type == Token.TEXTS:
                text_line = alignment_space[1] + "  " + token.token
            last_tok_type = token.tok_type
            text_line = text_line.strip('\n')
            print(text_line)


if __name__ == '__main__':
    out_str = ""
    for data in sys.stdin:
        out_str += data
    main(text=out_str)
