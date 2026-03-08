import re

from enum import Enum


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
