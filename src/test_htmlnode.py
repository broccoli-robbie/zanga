import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props2html(self):
        node = HTMLNode(
            "a",
            "This is a link",
            None,
            {"href": "https://boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://boot.dev" target="_blank"',
        )

    def test_2html(self):
        node = HTMLNode(
            "a",
            "This is a link",
            None,
            {
                "href": "https://boot.dev",
                "target": "_blank",
            },
        )
        node2 = HTMLNode(
            "p",
            "This is a paragraph",
            node,
        )
        with self.assertRaises(NotImplementedError):
            node2.to_html()

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()
