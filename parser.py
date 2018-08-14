from SequenceGenerator import SequenceGenerator


from bullet_generator import *

def main():
    l = ["*", "*", "*", "*", "**", "**", "***", "***", "***", "**", "*", "**", "**", "***"]

    #print(get_bullet(create_bullet(l)))

    text = '* This is an outline ' \
           '* This is the second numbered item in the outline ' \
           '** Lots ' \
           '** Less Numbers' \
           '*** Level 3 Star' \
           '*** Level 3 Star2' \
           '** Level 22'
    sq = SequenceGenerator(text=text)
    sq.parse()
    tokens = sq.token_list
    bullets = []
    text_line = ""
    for token in tokens:
        if token.tok_type == "token":
            bullets.append(token.token)
        elif token.tok_type == "text":
            bullet = get_bullet(create_bullet(bullets))
            text_line = bullet + " " + token.token
            print(text_line)


if __name__ == '__main__':
    main()
