import unittest

from delimiter import split_nodes_delimiter
from textnode import TextNode
from textnode import TextType


class TestDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "`", TextType.CODE),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_bold_delimiter(self):
        old_nodes = [TextNode("This is text with a *bold* word", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "*", TextType.BOLD),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_italic_delimiter(self):
        old_nodes = [TextNode("This is text with an _italic_ word", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "_", TextType.ITALIC),
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
