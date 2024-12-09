import unittest
from inline_markdown import split_nodes_delimiter, split_nodes_image,split_nodes_link, text_to_textnodes, extract_markdown_images, extract_markdown_links
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

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image] (https://imgur.com/gallery/magic-problems-require-modern-solutions-lMDz2vp)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                    [
                        TextNode("This is text with an ", TextType.TEXT),
                        TextNode("image", TextType.IMAGE, "https://i.imguhttps://i.imgur.com/zjjcJKZ.png"),
                    ],
                   new_nodes,
        )

        def test_split_image_alone(self):
            node = TextNode(
                "![image] (https://imgur.com/gallery/magic-problems-require-modern-solutions-lMDz2vp)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                        [
                            TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
                        ],
                        new_nodes,
                    )

        def test_split_image_multiple(self):
            node = TextNode(
                "This is text with an ![image](https://www.reddit.com/r/anime/comments/1bfiira/dandadan_new_key_visual/#lightbox) and another ![second image](https://www.imdb.com/title/tt5897304/mediaviewer/rm374999041/?ref_=tt_ov_i)",
                TextType.TEXT,
                )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "https://www.reddit.com/r/anime/comments/1bfiira/dandadan_new_key_visual/#lightbox"),
                    TextNode(" and another ", TextType.TEXT),
                        TextNode("second image", TextType.IMAGE, "https://www.imdb.com/title/tt5897304/mediaviewer/rm374999041/?ref_=tt_ov_i"),
                        ],
                new_nodes,
                )
        def test_split_links(self):
                node = TextNode(
                    "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
                    TextType.TEXT,
                )
                new_nodes = split_nodes_link([node])
                self.assertListEqual(
                    [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                        TextNode(" with text that follows", TextType.TEXT),
                    ],
                    new_nodes,
                )
        def test_text_to_textnodes(self):
            text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            nodes = text_to_textnodes(text)
            self.assertListEqual(
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ],
                nodes,
            )

if __name__ == "__main__":
    unittest.main()
