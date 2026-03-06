from textnode import TextNode, TextType
from extractor import extract_markdown_images
from extractor import extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        sections = old_node.text.split(delimiter)
        if len(sections) > 1:
            for index, section in enumerate(sections):
                if index % 2 == 0:
                    new_nodes.append(TextNode(section, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(section, text_type))
        else:
            raise ValueError("Invalid markdown syntax")
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        remaining_text = old_node.text
        for image in images:
            alt, url = image
            sections = remaining_text.split(f"![{alt}]({url})", 1)
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = sections[1]
        if remaining_text == "":
            continue
        else:
            raise ValueError("Invalid markdown syntax")
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        remaining_text = old_node.text
        for link in links:
            alt, url = link
            sections = remaining_text.split(f"[{alt}]({url})", 1)
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            remaining_text = sections[1]
        if remaining_text == "":
            continue
        else:
            raise ValueError("Invalid markdown syntax")
    return new_nodes
