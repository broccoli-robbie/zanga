import unittest

from splitter import split_nodes_delimiter
from splitter import split_nodes_image
from splitter import split_nodes_link
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


class TestImages(unittest.TestCase):
    def test_split_images(self):
        old_nodes = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
        ]
        self.assertListEqual(
            split_nodes_image(old_nodes),
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
        )


class TestLinks(unittest.TestCase):
    def test_split_links(self):
        old_nodes = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
            )
        ]
        self.assertListEqual(
            split_nodes_link(old_nodes),
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
        )


if __name__ == "__main__":
    unittest.main()
