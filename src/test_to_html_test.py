import unittest

from to_html import markdown_to_html_node

class TestToHtml(unittest.TestCase):
    
    def test_markdown_to_html_node(self):
        markdown = """
            # Hello, world!

            This is a paragraph with some **bold** and *italic* text.

            - Item 1
            - Item 2
            - Item 3

            > This is a quote.

            ![Alt text](https://example.com/image.jpg)
            """
        expected_html = """
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
            """


        # Convert markdown to HTML node
        html_node = markdown_to_html_node(markdown)
        
        # Convert the HTMLNode back to a string to compare with expected_html
        actual_html = html_node
        
        
        self.assertEqual(actual_html)

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

if __name__ == "__main__":
    unittest.main()
