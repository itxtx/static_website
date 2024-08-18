import os
import shutil
from to_html import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    static_dir = "static"  # Specify the source directory
    public_dir = "public"  # Specify the destination directory
    recursive_static_to_public(static_dir, public_dir)
    print("Done copying static files to the public folder.")
    
    #from content generate using template.html and write it to public/index.html.
    content_path = 'content'   
    template_path =  'template.html'
    dest_path = 'public'
    generate_pages_recursive(content_path, template_path, dest_path)

def recursive_static_to_public(src, dest):
    # Ensure the destination directory is empty before copying
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

    # Iterate over the items in the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path):
            # If the item is a directory, ensure it exists in the destination and recurse
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            recursive_static_to_public(src_path, dest_path)
        elif os.path.isfile(src_path):
            # If the item is a file, copy it to the corresponding destination directory
            shutil.copy2(src_path, dest_path)
            print(f"Copying {src_path} to {dest_path}")  # Logging

def extract_title(markdown):
    # pull line with # from the markdown file otherwise raise an exception
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:]
    raise Exception("No title found in the markdown file")
    



def generate_page(from_path, template_path, dest_path):
    # Read the content of the markdown file
    with open(from_path, "r") as file:
        text = file.read()
    node = markdown_to_html_node(text)
    title = extract_title(text)
    # Read the content of the template file
    with open(template_path, "r") as file:
        template = file.read()
    # Replace the placeholders in the template with the content and title
    #print(f"title: {title}; node: {node.to_html}\n")  
    template = template.replace("{{ Title }}",f"{title}")
    template = template.replace("{{ Content }}",f"{node.to_html()}")
    
    #print(f"Generated {dest_path}")
    #print(f"Generated {node.to_html()}")
    

    # Write the generated content to the destination file
    with open(dest_path, "w") as file:
        file.write(template)
    print(f"Generated {dest_path}")
    
    
    
    
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
##Crawl every entry in the content directory
##For each markdown file found, generate a new .html file using the same template.html. The generated pages should be written to the public directory in the same directory structure.
#os.listdir
#os.path.join
#os.path.isfile
#pathlib.Path

    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isdir(entry_path):
            generate_pages_recursive(entry_path, template_path, dest_dir_path)
        elif entry.endswith(".md"):
            # Generate the destination path for the new HTML file
            entry_name = os.path.splitext(entry)[0]
            dest_path = os.path.join(dest_dir_path, f"{entry_name}.html")
            generate_page(entry_path, template_path, dest_path)
            print(f"Generated {dest_path}")
        




















main()
