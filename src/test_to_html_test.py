import unittest
from htmlnode import ParentNode, LeafNode, HTMLNode
from to_html import markdown_to_html_node

class TestToHtml(unittest.TestCase):
    """
    def test_markdown_to_html_node(self):
        #markdown = 
            # Hello, world!

            This is a paragraph with some **bold** and *italic* text.

            - Item 1
            - Item 2
            - Item 3

            > This is a quote.

            ![Alt text](https://example.com/image.jpg)
            
        #expected_html =
            <div>
            <h1>Hello, world!</h1>
            <p>This is a paragraph with some <b>bold</b> and <i>italic</i> text.</p>
            <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
            </ul>
            <blockquote>This is a quote.</blockquote>
            <p><img src="https://example.com/image.jpg" alt="Alt text"/></p>
            </div>
            #


        # Convert markdown to HTML node
        html_node = markdown_to_html_node(markdown)
        
        # Convert the HTMLNode back to a string to compare with expected_html
        actual_html = html_node.to_html()
        
        
        self.assertEqual(actual_html, expected_html)
    """
    def test_empty_markdown(self):
        markdown = ""
        expected_html = "<div></div>"

        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()

        self.assertEqual(actual_html, expected_html)
    def test_link_markdown(self):
        markdown = " ![Alt text](https://example.com/image.jpg)"
        expected_html = '<div><p><img src="https://example.com/image.jpg" alt="Alt text"/></p></div>'

        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()

        self.assertEqual(actual_html, expected_html)

    def test_only_paragraph(self):
        markdown = "This is just a paragraph."
        expected_html = "<div><p>This is just a paragraph.</p></div>"

        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()

        self.assertEqual(actual_html, expected_html)

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item\n3. Third item"
        expected_html = (
            '<div>'
            '<ol>'
            '<li>First item</li>'
            '<li>Second item</li>'
            '<li>Third item</li>'
            '</ol>'
            '</div>'
        )

        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()

        self.assertEqual(actual_html, expected_html)

    def test_code_block(self):
        markdown = "```Code block here```"
        expected_html = (
            '<div>'
            '<pre><code>Code block here</code></pre>'
            '</div>'
        )

        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()

        self.assertEqual(actual_html, expected_html)
        
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
