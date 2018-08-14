from SequenceGenerator import SequenceGenerator


from bullet_generator import *

def main():
    l = ["*", "*", "*", "*", "**", "**", "***", "***", "***", "**", "*", "**", "**", "***"]
    node = get_bullet(l)
    print_tree(node)


if __name__ == '__main__':
    main()
