from htmlnode import HTMLNode, LeafNode, ParentNode
from split_delimiter import text_to_text_nodes, markdown_to_blocks, block_to_block_type, split_nodes_delimiter, split_nodes_link
from textnode import TextNode




def text_node_to_html_node(text_node):
    mapping = {
        "text": lambda tn: LeafNode(tn.text),
        "bold": lambda tn: LeafNode(tn.text, "b"),
        "italic": lambda tn: LeafNode(tn.text, "i"),
        "code": lambda tn: LeafNode(tn.text, "code"),
        "link": lambda tn: LeafNode(tn.text, "a", {"href": tn.url}),
        "image": lambda tn: LeafNode("", "img", {"src": tn.url, "alt": tn.text}),
    }

    if text_node.text_type in mapping:
        return mapping[text_node.text_type](text_node)
    else:
        raise Exception(f"Unknown text type: {text_node.text_type}")


def block_type_to_tag(block_type):
    if block_type == "paragraph":
        return "p"
    elif block_type == "heading":
        return f"h{block_type[-1]}"
    elif block_type == "code":
        return "pre"
    elif block_type == "unordered_list":
        return "ul"
    elif block_type == "ordered_list":
        return "ol"
    elif block_type == "list_item":
        return "li"
    elif block_type == "quote":
        return "blockquote"
    else:
        return None


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode(children, "div")
    

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == "paragraph":
        return paragraph_to_html_node(block)
    elif block_type == "heading":
        return heading_to_html_node(block)
    elif block_type == "code":
        return code_to_html_node(block)
    elif block_type == "unordered_list":
        return ullist_to_html_node(block)
    elif block_type == "ordered_list":
        return ollist_to_html_node(block)
    elif block_type == "quote":
        return quote_to_html_node(block)
    else:
        raise Exception(f"Unknown block type: {block_type}")
    

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children



def text_to_html_node(text):
    children = text_to_children(text)
    return ParentNode(children)




def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph.text)
    return ParentNode(children, "p")

def code_to_html_node(code):
    children = text_to_children(code.text)
    return ParentNode(children, "pre")

def heading_to_html_node(block, tag):
    children = text_to_children(block)
    return ParentNode(children, tag)

def ullist_to_html_node(block):
    items = block.split("\n")
    children = [ParentNode(text_to_children(item), "li") for item in items]
    return ParentNode(children, "ul")

def ollist_to_html_node(block):
    items = block.split("\n")
    children = [ParentNode(text_to_children(item), "li") for item in items]
    return ParentNode(children, "ol")

def quote_to_html_node(block):
    children = text_to_children(block)
    return ParentNode(children, "blockquote")