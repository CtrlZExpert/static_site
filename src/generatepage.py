import os
from pathlib import Path
from block_markdown import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)



def generate_page(from_path, template_path, dest_path):
    print(f"* {from_path} {template_path} -> {dest_path}")
    with open(from_path, 'r') as f:
        content = f.read()
    with open(template_path, 'r') as f:
        template = f.read()
    node = markdown_to_html_node(content)
    html = node.to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No h1 header found in the markdown.")
