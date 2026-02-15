from textnode import TextType
from textnode import TextNode


def main():
    node = TextNode("dummy", TextType.LINK, "boot.dev")
    print(node)


if __name__ == "__main__":
    main()
