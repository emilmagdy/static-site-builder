import unittest
from markdown_blocks import block_to_block_type,BlockType, markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )
        

    def test_block_to_blocktype(self):
        block1 ="## am in fact a Hobbit in all but size"
        block2 ="""> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien"""
        block3 ="""- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty"""
        block4 ="""1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn"""

        self.assertEqual(block_to_block_type(block1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block2), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(block3), BlockType.ULIST)
        self.assertEqual(block_to_block_type(block4), BlockType.OLIST)

        

        
