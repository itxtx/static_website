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

    # Handle images and links separately after text processing
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes


def extract_markdown_images(text):
    # Regular expression to find markdown images
    image_pattern = r'!\[([^\]]*)\]\((https?://[^\)]+)\)'
    images = re.findall(image_pattern, text)
    return images if images else None


def extract_markdown_links(text):
    # Regular expression to find markdown links
    link_pattern = r'\[([^\]]*)\]\((https?://[^\)]+)\)'
    links = re.findall(link_pattern, text)
    return links if links else None


def split_nodes_image2(old_nodes):
    text_type_image = "image"
    new_list = []
    
    for node in old_nodes:
        if node.text_type != "text":
            new_list.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_list.append(node)
            continue

        for (image_alt, image_link) in images:
            sections = text.split(f"![{image_alt}]({image_link})")
            for i, section in enumerate(sections):
                if section:
                    new_list.extend(parse_markdown_to_text_nodes(section))
                if i < len(sections) - 1:
                    new_list.append(TextNode(image_alt, text_type_image, image_link))
    
    return new_list


def split_nodes_link2(old_nodes):
    text_type_link = "link"
    new_list = []

    for node in old_nodes:
        if node.text_type != "text":
            new_list.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_list.append(node)
            continue

        for (alt, url) in links:
            sections = text.split(f"[{alt}]({url})")
            for i, section in enumerate(sections):
                if section:
                    new_list.extend(parse_markdown_to_text_nodes(section))
                if i < len(sections) - 1:
                    new_list.append(TextNode(alt, text_type_link, url))

    return new_list


def split_nodes_image(old_nodes):
    text_type_text = "text"
    text_type_image = "image"
    new_list = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_list.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_list.append(node)
            continue

        cursor = 0
        for image_alt, image_link in images:
            image_text = f"![{image_alt}]({image_link})"
            start_index = text.find(image_text, cursor)

            # Add text before the image
            if start_index > cursor:
                new_list.extend(parse_markdown_to_text_nodes(text[cursor:start_index]))

            # Add the image node
            new_list.append(TextNode(image_alt, text_type_image, image_link))

            # Update the cursor to the end of the current image
            cursor = start_index + len(image_text)

        # Add any remaining text after the last image
        if cursor < len(text):
            new_list.extend(parse_markdown_to_text_nodes(text[cursor:]))

    return new_list



def split_nodes_link(old_nodes):
    text_type_link = "link"
    new_list = []

    for node in old_nodes:
        if node.text_type != "text":
            new_list.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_list.append(node)
            continue

        cursor = 0
        for alt, url in links:
            link_text = f"[{alt}]({url})"
            start_index = text.find(link_text, cursor)

            # Add the text before the link as a text node
            if start_index > cursor:
                new_list.extend(parse_markdown_to_text_nodes(text[cursor:start_index]))

            # Add the link as a link node
            new_list.append(TextNode(alt, text_type_link, url))

            # Update the cursor position to after the current link
            cursor = start_index + len(link_text)

        # Add any remaining text after the last link
        if cursor < len(text):
            new_list.extend(parse_markdown_to_text_nodes(text[cursor:]))

    return new_list

