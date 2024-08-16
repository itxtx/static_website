import unittest

from split_delimiter import extract_markdown_images, extract_markdown_links, parse_markdown_to_text_nodes

class TestExtract(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        text = "![Image 1](https://example.com/image1.png) ![Image 2](https://example.com/image2.png)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("Image 1", "https://example.com/image1.png"), ("Image 2", "https://example.com/image2.png")])
        
    def test_extract_markdown_links(self):
        text = "[Link 1](https://example.com/link1) [Link 2](https://example.com/link2)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("Link 1", "https://example.com/link1"), ("Link 2", "https://example.com/link2")])
        


if __name__ == '__main__':
    unittest.main()
    