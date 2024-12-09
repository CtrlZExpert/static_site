block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        stripped_blocks.append(block.strip())
    return stripped_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if lines[0].startswith("#") and len(lines[0].split()[0]) <= 6 and  len(lines[0].split()) > 1:
        return block_type_heading
    elif block.startswith("```") and block.endswith("```"):
        return block_type_code
    elif all(line.lstrip().startswith(">") for line in lines):
        return block_type_quote
    elif all(line.lstrip().startswith(("* ", "- ")) for line in lines):
        return block_type_ulist
    elif all(line.lstrip().startswith(f"{i}.") for i, line in enumerate(lines, start=1)):
        return block_type_olist
    else:
        return block_type_paragraph

d
