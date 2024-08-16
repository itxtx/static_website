import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_eq_same_properties(self):
        node1 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")], {"class": "paragraph"})
        node2 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")], {"class": "paragraph"})
        self.assertEqual(node1.props_to_html(), node2.props_to_html())

    #def test_eq_different_tag(self):
    #    node1 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")], {"class": "paragraph"})
    #    node2 = HTMLNode("div", "This is a paragraph", [HTMLNode("b", "bold text")], {"class": "paragraph"})
   #     self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

    #def test_eq_different_value(self):
    #    node1 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")], {"class": "paragraph"})
    #    node2 = HTMLNode("p", "Different paragraph", [HTMLNode("b", "bold text")], {"class": "paragraph"})
    #    self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

    #def test_eq_different_children(self):
    #    node1 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")], {"class": "paragraph"})
    #    node2 = HTMLNode("p", "This is a paragraph", [HTMLNode("i", "italic text")], {"class": "paragraph"})
    #    self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

    def test_eq_different_props(self):
        node1 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")], {"class": "paragraph"})
        node2 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")], {"class": "different"})
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

    def test_eq_none_props(self):
        node1 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")])
        node2 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")])
        self.assertEqual(node1.props_to_html(), node2.props_to_html())

    def test_eq_props_vs_none_props(self):
        node1 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")], {"class": "paragraph"})
        node2 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")])
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

    def test_eq_none_children(self):
        node1 = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node1.props_to_html(), node2.props_to_html())

    #def test_eq_children_vs_none_children(self):
    #    node1 = HTMLNode("p", "This is a paragraph", [HTMLNode("b", "bold text")])
    #    node2 = HTMLNode("p", "This is a paragraph")
    #    self.assertNotEqual(node1.props_to_html(), node2.props_to_html())


class TestLeafNode(unittest.TestCase):

    def test_eq_same_properties(self):
        node1 = LeafNode("b", "bold text", {"class": "bold"})
        node2 = LeafNode("b", "bold text", {"class": "bold"})
        self.assertEqual(node1.to_html(), node2.to_html())

    def test_eq_different_tag(self):
        node1 = LeafNode("b", "bold text", {"class": "bold"})
        node2 = LeafNode("i", "bold text", {"class": "bold"})
        self.assertNotEqual(node1.to_html(), node2.to_html())

    def test_eq_different_value(self):
        node1 = LeafNode("b", "bold text", {"class": "bold"})
        node2 = LeafNode("b", "italic text", {"class": "bold"})
        self.assertNotEqual(node1.to_html(), node2.to_html())

    def test_eq_different_props(self):
        node1 = LeafNode("b", "bold text", {"class": "bold"})
        node2 = LeafNode("b", "bold text", {"class": "different"})
        self.assertNotEqual(node1.to_html(), node2.to_html())

    def test_eq_none_props(self):
        node1 = LeafNode("b", "bold text")
        node2 = LeafNode("b", "bold text")
        self.assertEqual(node1.to_html(), node2.to_html())

    def test_eq_props_vs_none_props(self):
        node1 = LeafNode("b", "bold text", {"class": "bold"})
        node2 = LeafNode("b", "bold text")
        self.assertNotEqual(node1.to_html(), node2.to_html())


class TestParentNode(unittest.TestCase):

    def test_eq_same_properties(self):
        node1 = ParentNode("p", [LeafNode("b", "bold text")], {"class": "paragraph"})
        node2 = ParentNode("p", [LeafNode("b", "bold text")], {"class": "paragraph"})
        self.assertEqual(node1.to_html(), node2.to_html())
        

   # def test_eq_different_tag(self):
    #    node1 = ParentNode("p", [LeafNode("b", "bold text")], {"class": "paragraph"})
    #    node2 = ParentNode("div", [LeafNode("b", "bold text")], {"class": "paragraph"})
    #    self.assertNotEqual(node1.to_html(), node2.to_html())

    def test_eq_different_children(self):
        node1 = ParentNode("p", [LeafNode("b", "bold text")], {"class": "paragraph"})
        node2 = ParentNode("p", [LeafNode("i", "italic text")], {"class": "paragraph"})
        self.assertNotEqual(node1.to_html(), node2.to_html())

    def test_eq_different_props(self):
        node1 = ParentNode("p", [LeafNode("b", "bold text")], {"class": "paragraph"})
        node2 = ParentNode("p", [LeafNode("b", "bold text")], {"class": "different"})
        self.assertNotEqual(node1.to_html(), node2.to_html())

    def test_eq_none_props(self):
        node1 = ParentNode("p", [LeafNode("b", "bold text")])
        node2 = ParentNode("p", [LeafNode("b", "bold text")])
        self.assertEqual(node1.to_html(), node2.to_html())

    def test_eq_props_vs_none_props(self):
        node1 = ParentNode("p", [LeafNode("b", "bold text")], {"class": "paragraph"})
        node2 = ParentNode("p", [LeafNode("b", "bold text")])
        self.assertNotEqual(node1.to_html(), node2.to_html())


    def test_assertion_error_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "bold text")], {"class": "paragraph"})
    
    def test_assertion_error_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None, {"class": "paragraph"}).to_html()
            









if __name__ == "__main__":
    unittest.main()
