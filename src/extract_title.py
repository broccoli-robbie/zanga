from block_markdown import block_to_block_type, markdown_to_blocks, BlockType


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    text = ""
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            heading = block.split(" ", maxsplit=1)
            if len(heading) == 2 and heading[0] == "#":
                return heading[1].strip()
    raise Exception("no markdown title found")
