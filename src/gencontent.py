import os

from pathlib import Path
from block_markdown import markdown_to_html_node


def generate_page(src_path, template_path, dst_path, basepath):
    print(f"Generating page from {src_path} to {dst_path} using {template_path}.")

    with open(src_path, "r") as src:
        md = src.read()

    with open(template_path, "r") as template:
        temp = template.read()

    node = markdown_to_html_node(md)
    html = node.to_html()

    title = extract_title(md)
    temp = (
        temp.replace("{{ Title }}", title)
        .replace("{{ Content }}", html)
        .replace("href='/", f"href='{basepath}")
        .replace("src='/", f"src={basepath}")
    )

    dst_dir = os.path.dirname(dst_path)
    if dst_dir:
        os.makedirs(dst_dir, exist_ok=True)

    with open(dst_path, "w") as dst:
        dst.write(temp)


def generate_pages_recursive(src_path_content, template_path, dst_dir_path, basepath):
    for file in os.listdir(src_path_content):
        src_path = os.path.join(src_path_content, file)
        dst_path = os.path.join(dst_dir_path, file)
        if os.path.isfile(src_path):
            dst_path = Path(dst_path).with_suffix(".html")
            generate_page(src_path, template_path, dst_path, basepath)
        else:
            generate_pages_recursive(src_path, template_path, dst_path, basepath)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no markdown title found")
