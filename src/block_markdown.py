import re

from enum import Enum

from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"


def block_to_block_type(block):
    if re.match(r"^#{1,6}\s", block):
        return BlockType.HEADING
    elif re.match(r"^`{3}\n.+\n`{3}$", block, flags=re.DOTALL):
        return BlockType.CODE
    elif re.match(r"^>", block):
        return BlockType.QUOTE
    elif re.match(r"^-\s", block):
        return BlockType.UL
    elif re.match(r"^\d+\.\s", block):
        return BlockType.OL
    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UL:
        return ul_to_html_node(block)
    if block_type == BlockType.OL:
        return ol_to_html_node(block)
    raise ValueError("invalid block type")


# Helper Functions
def text_to_children(text):
    textnodes = text_to_textnodes(text)
    new_nodes = []
    for node in textnodes:
        html_node = text_node_to_html_node(node)
        new_nodes.append(html_node)
    return new_nodes


def paragraph_to_html_node(block):
    paragraph = block.replace("\n", " ")
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    heading = block.split(" ", maxsplit=1)
    tag = "h" + str(len(heading[0]))
    text = heading[1]
    children = text_to_children(text)
    return ParentNode(tag, children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block.removeprefix("```\n")
    child = text.removesuffix("```")
    code = ParentNode("code", [LeafNode(None, child)])
    return ParentNode("pre", [code])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def ul_to_html_node(block):
    items = []
    for item in block.split("\n"):
        text = item.removeprefix("- ")
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)


def ol_to_html_node(block):
    items = []
    for item in block.split("\n"):
        text = item.split(". ", maxsplit=1)
        children = text_to_children(text[1])
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)
