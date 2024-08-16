from textnode import TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_type_text = "text"
    
    new_list = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_list.append(node)
            continue

        # Split the text by the delimiter
        parts = node.text.split(delimiter)

        for i, part in enumerate(parts):
            if part:
                current_text_type = text_type if i % 2 == 1 else text_type_text
                new_list.append(TextNode(part, current_text_type))

        # Check for unclosed delimiters
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter {delimiter} found in text: {node.text}")

    return new_list


def parse_markdown_to_text_nodes(markdown_text):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"

        

    # Start with a single node containing all text
    nodes = [TextNode(markdown_text, text_type_text)]

    # Handle each type of delimiter
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)

                                  

    return nodes


def extract_markdown_images(text):
    # Regular expression to find markdown images
    image_pattern = r'!\[([^\]]*)\]\((https?://[^\)]+)\)'
    images = re.findall(image_pattern, text)
    return images

def extract_markdown_links(text):
    # Regular expression to find markdown links
    link_pattern = r'\[([^\]]*)\]\((https?://[^\)]+)\)'
    links = re.findall(link_pattern, text)
    return links














def split_nodes_image(old_nodes):
    text_type_text = "text"
    text_type_image = "image"
    
    image_pattern = r'(!\[.*?\]\(.*?\))'  # Pattern to match markdown images
    new_list = []
    
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_list.append(node)
            continue
        
        parts = re.split(image_pattern, node.text)  # Split text based on the image pattern

        for part in parts:
            if not part:
                continue
            
            match = re.match(image_pattern, part)
            if match:
                alt_text, url = extract_markdown_images(part)[0]
                new_list.append(TextNode(alt_text, text_type_image, url))
            else:
                new_list.append(TextNode(part, text_type_text))
                    
    return new_list
        
    
    
    
    
    
def split_nodes_link(old_nodes):
    text_type_text = "text"
    text_type_link = "link"
    link_pattern = r'(\[.*?\]\(.*?\))' # r'\[([^\]]*)\]\((https?://[^\)]+)\)'
    
    new_list = []
    
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_list.append(node)
            continue

        parts = re.split(link_pattern, node.text)
        
        for part in parts:
            if part:
                match = re.match(link_pattern, part)
                if match:
                    alt_text, url = match.groups()
                    new_list.append(TextNode(alt_text, text_type_link, url))
                else:
                    new_list.append(TextNode(part, text_type_text))
                    
    return new_list    
    
    
    
    
