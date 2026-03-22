import os

from block_markdown import markdown_to_html_node
from extract_title import extract_title


def generate_page(src_path, template_path, dst_path):
    print(f"Generating page from {src_path} to {dst_path} using {template_path}.")

    # Read markdown file
    with open(src_path, "r") as src:
        md = src.read()

    # Read template file
    with open(template_path, "r") as template:
        temp = template.read()

    # Convert markdown to HTML
    node = markdown_to_html_node(md)
    html = node.to_html()

    # Extract markdown title
    title = extract_title(md)

    # Replace placeholders in template
    temp = temp.replace("{{ Title }}", title).replace("{{ Content }}", html)

    # Create directories
    dst_dir = os.path.dirname(dst_path)
    if dst_dir:
        os.makedirs(dst_dir, exist_ok=True)

    # Write HTML file
    with open(dst_path, "w") as dst:
        dst.write(temp)
