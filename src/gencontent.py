import os

from block_markdown import markdown_to_html_node


def generate_page(src_path, template_path, dst_path):
    print(f"Generating page from {src_path} to {dst_path} using {template_path}.")

    with open(src_path, "r") as src:
        md = src.read()

    with open(template_path, "r") as template:
        temp = template.read()

    node = markdown_to_html_node(md)
    html = node.to_html()

    title = extract_title(md)
    temp = temp.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dst_dir = os.path.dirname(dst_path)
    if dst_dir:
        os.makedirs(dst_dir, exist_ok=True)

    with open(dst_path, "w") as dst:
        dst.write(temp)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no markdown title found")
