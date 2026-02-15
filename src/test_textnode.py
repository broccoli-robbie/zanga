import unittest

from textnode import TextNode
from textnode import TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_difftext(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_difftype(self):
        node = TextNode("This is bold text", TextType.BOLD)
        node2 = TextNode("This is italic text", TextType.ITALIC)
        self.assertFalse(node.text_type == node2.text_type)

    def test_nourl(self):
        node = TextNode("This is NOT a url", TextType.TEXT)
        self.assertTrue(node.url is None)


if __name__ == "__main__":
    unittest.main()
