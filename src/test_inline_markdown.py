import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_links, extract_markdown_images
from textnode import  TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_valid_delimiters(self):
        node = TextNode("This is text with `code` block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" block", TextType.TEXT)
            ]

        )

def test_no_delimiters(self):
    node = TextNode("Unbalance 'code", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertNotEqual(new_nodes, "`")
    def test_extract_markdown_images(self):
            matches = extract_markdown_images(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                    ("link", "https://boot.dev"),
                    ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )
if __name__ == "__main__":
    unittest.main()
