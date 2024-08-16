
import unittest

from split_delimiter import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        text = "# This is a heading\n\n This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item"
        compare = ["# This is a heading","This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks, compare)

    def test_markdown_to_blocks_no_heading(self):
        text = "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item"
        compare = ["This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks, compare)
        
    def test_markdown_to_blocks_no_paragraph(self):
        text = "# This is a heading\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        compare = ["# This is a heading","* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks, compare)
    
    def test_markdown_to_blocks_check_whitespace(self):
        text = "# This is a heading\n\n\n\n\n                                              This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n"
        compare = ["# This is a heading","This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks, compare)
        
class TestBlockToBlockType(unittest.TestCase):
    
    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "heading")
        
    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")
        
    def test_block_to_block_type_unordered_list(self):
        block = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "unordered_list")
        
    def test_block_to_block_type_unordered_list2(self):
        block = "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "unordered_list")
    
    def test_block_to_block_type_ordered_list(self):
        block = "1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "ordered_list")
        
    def test_block_to_block_type_ordered_list2(self):
        block = "1. This is the first list item in a list block\n1. This is a list item\n1. This is another list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")
        
    def test_block_to_block_type_code(self):
        block = "`This is a code block`"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "code")
        
    def test_block_to_block_type_quote(self):
        block = "> This is a quote block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "quote")
        
    

if __name__ == '__main__':
    unittest.main()