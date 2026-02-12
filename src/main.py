from textnode import TextType
from textnode import TextNode


def main():
    text_node = TextNode("dummy", TextType("bold"), "boot.dev")
    print(text_node)
    return


if __name__ == "__main__":
    main()
