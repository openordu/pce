import json
import os
import re
from pathlib import Path
from unidecode import unidecode

def sanitize_filename(filename):
    return re.sub(r'[^\w\-_]', '_', filename)

def write_md_file(json_data, filename):

    name = json_data.get("name","")
    text = json_data.get("text","")
    attributes = json_data.get("attributes","")
    entities = json_data.get("entities","")
    sources = json_data.get("sources","")
    order = json_data.get("order",0)
    image = json_data.get("images",[None])
    entityimage = None
    # if the key is not images, try image
    if image[0] == None:
        image = json_data.get("image",[None])
    if image[0] != None:
        entityimage = image[0]

    with open(filename, "w") as md_file:
        md_file.write("---\n")
        md_file.write("layout: layouts/pce.njk\n")
        md_file.write(f"title: {name}\n")
        md_file.write(f"icon: file-lines\n")
        md_file.write(f"order: {order}\n")
        md_file.write(f"contributors: [ 'Christopher Godwin' ]\n")

        md_file.write("attributes:\n")
        for attr in attributes:
            md_file.write(f"  - {attr.get('entity', '')} {attr.get('attribute', '')}\n")

        md_file.write("categories:\n")
        for type in set([i.get('type','') for i in entities]):
            md_file.write(f"  - {type}\n")
        
        md_file.write("entities:\n")
        for ent in entities:
            md_file.write(f"  - {ent.get('entity', '')}({ent.get('type', '')})\n")
        md_file.write("tags:\n")
        for ent in entities:
            md_file.write(f"  - {ent.get('entity', '')}\n")
        md_file.write("---\n")

        md_file.write("``` tab [group1:Info]\n")
        md_file.write("::: magazinestyle\n")
        md_file.write(f"{text}\n\n")
        md_file.write(":::\n")
        md_file.write("```\n")

        md_file.write("``` tab [group1:Attributes]\n")
        for attr in attributes:
            try: md_file.write(f"- **{attr['entity']}**: {attr['attribute']}\n")
            except KeyError as e:
                print(e)
                md_file.write(f"- **Attribute**: {attr['attribute']}\n")
        md_file.write("```\n")

        md_file.write("``` tab [group1:Entities]\n")
        for ent in entities:
            try: md_file.write(f"- **{ent['entity']}**: {ent['type']}\n")
            except KeyError as e:
                print(e)
                md_file.write(f"- **entities**: {ent['text']}\n")
        md_file.write("```\n")

        md_file.write("``` tab [group1:Sources]\n")
        for src in sources:
            md_file.write(f"- {src}\n")
        md_file.write("```\n")
        if entityimage != None: md_file.write(f"![{name} Image]({entityimage})\n")

def process_json_files():
    input_dir = "entries"
    output_dir = "./"
    index_file = "index.sjson"

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    with open(index_file, "r") as json_file:
        index_data = json.load(json_file)

    # Keep track of the files in each directory
    dir_files = dict()

    for i, entry in enumerate(index_data):
        sanitized_entry = sanitize_filename(entry)
        if not sanitized_entry:
            print(f"Skipping empty entry at index {i}")
            continue
        sub_dir = unidecode(sanitized_entry[0]).upper()
        input_file = os.path.join(input_dir, sanitized_entry + ".json")
        output_sub_dir = os.path.join(output_dir, sub_dir)
        Path(output_sub_dir).mkdir(parents=True, exist_ok=True)
        output_file = os.path.join(output_sub_dir, sanitized_entry + ".md")

        if os.path.isfile(input_file):
            with open(input_file, "r") as json_file:
                print(f'Processing input file: {input_file}')
                json_data = json.load(json_file)
                json_data["order"] = i
                write_md_file(json_data, output_file)

                # Add the file to the list for its directory
                if sub_dir not in dir_files:
                    dir_files[sub_dir] = []
                dir_files[sub_dir].append(sanitized_entry)
        else:
            print(f"File not found: {input_file}")

    # Write index.md for each directory
    for sub_dir, files in dir_files.items():
        with open(os.path.join(output_dir, sub_dir, "index.md"), "w") as index_file:
            index_file.write("---\n")
            index_file.write(f"title: Volume {sub_dir}\n")
            index_file.write("layout: layouts/pce.njk\n")
            index_file.write("---\n")
            for file in files:
                index_file.write(f"- [{file}]({file})\n")

if __name__ == "__main__":
    process_json_files()