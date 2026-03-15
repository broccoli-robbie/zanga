import re

from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered list"
    OL = "ordered list"


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


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    new_nodes = []
    for node in textnodes:
        new_nodes.append(text_node_to_html_node(node))
    return new_nodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.QUOTE:
            lines = [line.removeprefix("> ") for line in block.split("\n")]
            content = " ".join(lines)
            child_nodes.append(ParentNode("blockquote", text_to_children(content)))

        elif block_type == BlockType.UL:
            items = []
            for item in block.split("\n"):
                items.append(
                    ParentNode("li", text_to_children(item.removeprefix("- ")))
                )
            child_nodes.append(ParentNode("ul", items))

        elif block_type == BlockType.OL:
            items = []
            for item in block.split("\n"):
                items.append(
                    ParentNode("li", text_to_children(item.split(". ", maxsplit=1)[1]))
                )
            child_nodes.append(ParentNode("ol", items))

        elif block_type == BlockType.CODE:
            text = block.removeprefix("```\n")
            code = text.removesuffix("```")
            child_nodes.append(ParentNode("pre", [LeafNode("code", code)]))

        elif block_type == BlockType.HEADING:
            heading = block.split(" ", maxsplit=1)
            tag = "h" + str(len(heading[0]))
            child_nodes.append(ParentNode(tag, text_to_children(heading[1])))

        elif block_type == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            child_nodes.append(ParentNode("p", text_to_children(block)))

    parent_html_node = ParentNode("div", child_nodes)
    return parent_html_node
