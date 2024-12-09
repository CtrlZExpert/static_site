import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_olist,
    block_type_ulist,
    block_type_quote,
)

class  TestMarkdownToHTML(unittest.TestCase):
    def  test_markdown_to_block(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
            blocks
        )

    def test_markdown_to_blocks_newlines(self):
            markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
    """
            blocks = markdown_to_blocks(markdown)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                    "* This is a list\n* with items",
                ],
            )

    def test_block_to_heading(self):
        text = "### This a heading"
        text2 = "# This is another heading"
        text3 = "###### This is also a heading"
        heading = block_to_block_type(text)
        heading2 = block_to_block_type(text2)
        heading3 = block_to_block_type(text3)
        self.assertEqual( block_type_heading, heading)
        self.assertEqual( block_type_heading, heading2)
        self.assertEqual( block_type_heading, heading3)
    def test_block_code(self):
        text = "```This is a block of code```"
        code = block_to_block_type(text)
        self.assertEqual(block_type_code, code)

    def test_block_to_unorder_list(self):
        block = "* This order list\n- Item\n- Another Item"
        unorder_list = block_to_block_type(block)
        self.assertEqual(block_type_ulist, unorder_list)
    def test_block_to_quotes(self):
        text = ">'This a quote.'"
        quote = block_to_block_type(text)
        self.assertEqual(block_type_quote, quote)
    def test_order_list(self):
        text ="""1. item
2. item
3.item"""
        ordered_list = block_to_block_type(text)
        self.assertEqual(block_type_olist, ordered_list)

if __name__ == "__main__":
    unittest.main()
