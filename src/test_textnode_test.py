import unittest

from textnode import TextNode



class TestTextNode(unittest.TestCase):
    def test_eq_same_properties(self):
        node1 = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", "http://example.com")
        self.assertEqual(node1, node2)

    def test_eq_different_text(self):
        node1 = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("Different text", "bold", "http://example.com")
        self.assertNotEqual(node1, node2)
    
    def test_eq_different_text_type(self):
        node1 = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "italic", "http://example.com")
        self.assertNotEqual(node1, node2)
    
    def test_eq_different_url(self):
        node1 = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", "http://different.com")
        self.assertNotEqual(node1, node2)
    
    def test_eq_none_url(self):
        node1 = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node1, node2)
    
    def test_eq_url_vs_none_url(self):
        node1 = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
