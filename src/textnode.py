from enum import Enum


class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    PLAIN = "plain"


class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = TextType(text_type)

        if url is None:
            self.url = None
        self.url = url

    def __eq__(self, other):
        if (
            (other.text == self.text)
            & (other.text_type == self.text_type)
            & (other.url == self.url)
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
