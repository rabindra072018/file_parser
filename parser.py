from SequenceGenerator import SequenceGenerator

from bullet_generator import *


def get_dot_alignment(alignment=None):
    alignment_count = len(alignment)
    alignment_symbol = {0: "-", 1: "+"}
    final_string = " "*alignment_count + str(alignment_symbol[alignment_count % 2])
    return final_string


def main():
    #l = ["*", "*", ".", "..", "...", "*", "**", "**", "***", "***", "***", "**", "*", "**", "**", "***"]

    #print(get_bullet(create_bullet(l)))

    text = '* This is an outline ' \
           '. Its not a very good outline1' \
           '.. Its not a very good outline2' \
           '... Its not a very good outline3' \
           '* This is the second numbered item in the outline ' \
           '** Lots ' \
           '** Less Numbers' \
           '*** Level 3 Star' \
           '. Its not a very good outline50' \
           '. Its not a very good outline51' \
           '. Its not a very good outline52' \
           '*** Level 3 Star2' \
           '** Level 22'
    sq = SequenceGenerator(text=text)
    sq.parse()
    tokens = sq.token_list
    bullets = []
    text_line = ""
    align_ment = ""
    last_tok_type = ""

    for token in tokens:
        if token.tok_type == "stars":
            bullets.append(token.token)
            last_tok_type = "stars"
            align_ment = ""
        elif token.tok_type == "dots":
            align_ment = get_dot_alignment(token.token)
            last_tok_type = "dots"
        elif token.tok_type == "text":
            if last_tok_type == "stars":
                bullet = get_bullet(create_bullet(bullets))
                text_line = bullet + " " + token.token
            elif last_tok_type == "dots":
                text_line = align_ment + token.token

            print(text_line)


if __name__ == '__main__':
    main()
