from htmlnode import HTMLNode, LeafNode, ParentNode
from split_delimiter import text_to_text_nodes, markdown_to_blocks, block_to_block_type, split_nodes_delimiter, split_nodes_link
from textnode import TextNode


def text_node_to_html_node(text_node):
    mapping = {
        "text": lambda tn: LeafNode(None, tn.text),
        "bold": lambda tn: LeafNode("b",tn.text),
        "italic": lambda tn: LeafNode( "i",tn.text),
        "code": lambda tn: LeafNode( "code",tn.text),
        "link": lambda tn: LeafNode( "a",tn.text, {"href": tn.url}),
        "image": lambda tn: LeafNode( "img","", {"src": tn.url, "alt": tn.text}),
    }
    #print(f"Processing text node: {text_node} as {mapping[text_node.text_type](text_node)}")
    if text_node.text_type in mapping:
        #print(f"Processing text node: {text_node} as {mapping[text_node.text_type](text_node)}\n")
        return mapping[text_node.text_type](text_node)
    else:
        raise Exception(f"Unknown text type: {text_node.text_type}")


def block_type_to_tag(block_type):
    tags = {
        "paragraph": "p",
        "heading": lambda level: f"h{level}",
        "code": "pre",
        "unordered_list": "ul",
        "ordered_list": "ol",
        "list_item": "li",
        "quote": "blockquote"
    }
    return tags.get(block_type, None)





def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div",children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    #print(f"\n\n----------------------------------------------------------------\n\nProcessing block: {block}, detected type: {block_type}")
    if block_type == "heading":
        return heading_to_html_node(block)
    elif block_type in ["paragraph", "code", "unordered_list", "ordered_list", "quote"]:
        function_mapping = {
            "paragraph": paragraph_to_html_node,
            "code": code_to_html_node,
            "unordered_list": ulist_to_html_node,
            "ordered_list": olist_to_html_node,
            "quote": quote_to_html_node,
        }
        return function_mapping[block_type](block)
    else:
        raise Exception(f"Unknown block type: {block_type}")


def text_to_children(text):
    
    text_nodes = text_to_text_nodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    #print(f"Processing text: {text} children: {children}")
    return children


def text_to_html_node(text):
    children = text_to_children(text)
    return ParentNode(None, children)


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)  # This is a string
    children = text_to_children(paragraph)  # Pass the string directly
    #print(f"Processing heading block: {block} as {ParentNode("p", children)}")
    return ParentNode("p", children)



def heading_to_html_node(block):
    level = block.count("#", 0, block.find(" "))  # Calculate heading level
    if level == 0 or level > 6:
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:].strip()
    children = text_to_children(text)
    #print(f"Processing heading block: {block} as {ParentNode(f"h{level}",children)}")
    return ParentNode(f"h{level}",children)


def code_to_html_node(block):
    if not (block.startswith("```") or block.endswith("```")):
        raise ValueError("Invalid code block")
    text = block[3:-3].strip()
    code_node = LeafNode("code",text)
    #print(f"Processing heading block: {block} as {ParentNode("pre",[code_node])}")
    return ParentNode("pre",[code_node])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[item.find(".") + 2:].strip()  # Strip leading numbering
        children = text_to_children(text)
        html_items.append(ParentNode("li",children))
    #print(f"Processing heading block: {block} as {ParentNode("ol",html_items)}")
    return ParentNode("ol",html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:].strip()  # Strip leading bullet
        children = text_to_children(text)
        html_items.append(ParentNode("li",children))
    #print(f"Processing heading block: {block} as {ParentNode("ul",html_items)}")
    return ParentNode("ul",html_items)



def quote_to_html_node(block):
    lines = block.split("\n")
    cleaned_lines = [line.lstrip(">").strip() for line in lines if line.startswith(">")]
    content = " ".join(cleaned_lines)
    children = text_to_children(content)
    #print(f"Processing heading block: {block} as {ParentNode("blockquote",children)}")
    return ParentNode("blockquote",children)
