import unittest
from to_html import text_node_to_html_node
from textnode import TextNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("This is a paragraph", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is a paragraph")
        
    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This is a paragraph", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>This is a paragraph</b>")
        
    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("This is a paragraph", "italic")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>This is a paragraph</i>")
    
    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This is a paragraph", "code")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>This is a paragraph</code>")
        
    def test_text_node_to_html_node_unknown(self):
        text_node =TextNode("This is a paragraph", "unknown")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)
            
            
    def test_text_node_to_html_node_link(self):
        text_node = TextNode("This is a paragraph", "link", url="http://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="http://example.com">This is a paragraph</a>')
    
    def test_text_node_to_html_node_image(self):
        text_node = TextNode("This is a paragraph", "image", url="http://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="http://example.com" alt="This is a paragraph"></img>')
        
    
if __name__ == "__main__":
    unittest.main()