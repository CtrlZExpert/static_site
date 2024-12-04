import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

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

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_to_html_with_children(self):
        child_node = LeafNode("p","This is a child.")
        parent_node = ParentNode("section", [child_node])
        self.assertEqual(parent_node.to_html(), "<section><p>This is a child.</p></section>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b","This is a grandchild.")
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("section",[child_node])
        self.assertEqual(parent_node.to_html(), "<section><p><b>This is a grandchild.</b></p></section>")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")



if __name__ == "__main__":
    unittest.main()
