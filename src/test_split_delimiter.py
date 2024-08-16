import unittest

from split_delimiter import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_text_nodes, markdown_to_blocks



text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"





class TestSplitDelimiter(unittest.TestCase):
    
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        compare = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, compare)
        
    def test_split_nodes_delimiter_no_delimiter(self):
        node = TextNode("This is text with a code block word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        compare = [node]
        self.assertEqual(new_nodes, compare)    
        
    def test_split_nodes_delimiter_multiple_delimiters(self):
        node = TextNode("This is text with a `code block` word `code block`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        compare = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word ", text_type_text),
            TextNode("code block", text_type_code),
        ]
        self.assertEqual(new_nodes, compare)
        
    def test_split_nodes_delimiter_multiple_different_delimiters(self):
        node = TextNode("This is text with a `code block` word **bold text** `code block`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        new_nodes = split_nodes_delimiter(new_nodes, "**", text_type_bold)
        compare = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word ", text_type_text),
            TextNode("bold text", text_type_bold),
            TextNode(" ", text_type_text),
            TextNode("code block", text_type_code),
        ]
        self.assertEqual(new_nodes, compare)


class TestSplitImage(unittest.TestCase):
    
    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](https://example.com/image.png)", text_type_text)
        new_nodes = split_nodes_image([node])
        compare = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://example.com/image.png"),
        ]
        self.assertEqual(new_nodes, compare)
        
    def test_split_nodes_image_no_image(self):
        node = TextNode("This is text with an image", text_type_text)
        new_nodes = split_nodes_image([node])
        compare = [node]
        self.assertEqual(new_nodes, compare)
    
    def test_split_nodes_image_multiple_images(self):
        node = TextNode("This is text with an ![image](https://example.com/image.png) ![image](https://example.com/image2.png)", text_type_text)
        new_nodes = split_nodes_image([node])
        compare = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://example.com/image.png"),
            TextNode(" ", text_type_text),
            TextNode("image", text_type_image, "https://example.com/image2.png"),
        ]
        self.assertEqual(new_nodes, compare)
        
    def test_split_nodes_image_multiple_different_nodes(self):
        
        node = TextNode("This is text with an ![image](https://example.com/image.png) **bold text** ![image](https://example.com/image2.png)", text_type_text)
        new_nodes = split_nodes_image([node])
        compare = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://example.com/image.png"),
            TextNode(" ", text_type_text),
            TextNode("bold text", text_type_bold),
            TextNode(" ", text_type_text),
            TextNode("image", text_type_image, "https://example.com/image2.png"),
        ]
        self.assertEqual(new_nodes, compare)
        
class TestSplitLink(unittest.TestCase):
    
    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](https://example.com/link)", text_type_text)
        new_nodes = split_nodes_link([node])
        compare = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link,"https://example.com/link"),
        ]
        self.assertEqual(new_nodes, compare)
        
    def test_split_nodes_link_no_link(self):
        node = TextNode("This is text with a link", text_type_text)
        new_nodes = split_nodes_link([node])
        compare = [node]
        self.assertEqual(new_nodes, compare)
        
    def test_split_nodes_link_multiple_links(self):
        node = TextNode("This is text with a [link](https://example.com/link) [link](https://example.com/link2)", text_type_text)
        new_nodes = split_nodes_link([node])
        compare = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link,"https://example.com/link"),
            TextNode(" ", text_type_text),
            TextNode("link", text_type_link,"https://example.com/link2"),
        ]
        self.assertEqual(new_nodes, compare)
        
    def test_split_nodes_link_multiple_different_nodes(self):
        node = TextNode("This is text with a [link](https://example.com/link) **bold text** [link](https://example.com/link2)", text_type_text)
        new_nodes = split_nodes_link([node])
        compare = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link,"https://example.com/link"),
            TextNode(" ", text_type_text),
            TextNode("bold text", text_type_bold),
            TextNode(" ", text_type_text),
            TextNode("link", text_type_link,"https://example.com/link2"),
        ]
        self.assertEqual(new_nodes, compare)
        
class Test_parse(unittest.TestCase):
    
    def test_parse_markdown_to_text_nodes(self):
        text = "This is **bold** and *italic* and `code` and [link](https://example.com/link) and ![image](https://example.com/image.png)"
        nodes = text_to_text_nodes(text)
        compare = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" and ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" and ", text_type_text),
            TextNode("link", text_type_link, "https://example.com/link"),
            TextNode(" and ", text_type_text),
            TextNode("image", text_type_image, "https://example.com/image.png"),
        ]
        self.assertEqual(nodes, compare)
    


if __name__ == "__main__":
    unittest.main()