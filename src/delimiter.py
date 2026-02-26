from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        nodes = old_node.text.split(delimiter)
        if len(nodes) > 1:
            for index, node in enumerate(nodes):
                if index % 2 == 0:
                    new_nodes.append(TextNode(node, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(node, text_type))
        else:
            raise ValueError("Invalid markdown syntax")
    return new_nodes
