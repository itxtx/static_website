import os
import shutil
from to_html import markdown_to_html_node



def main():
    static_dir = "static"  # Specify the source directory
    public_dir = "public"  # Specify the destination directory
    recursive_static_to_public(static_dir, public_dir)
    print("Done copying static files to the public folder.")
    
    #from content generate using template.html and write it to public/index.html.
    from_path = 'content/index.md'   
    template_path =  'template.html'
    dest_path = 'public/index.html'
    generate_page(from_path, template_path, dest_path)

def recursive_static_to_public(src, dest):
    # Ensure the destination directory is empty before copying
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

    # Iterate over the items in the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copying {src_path} to {dest_path}")  # Logging
        else:
            # Recursively copy directories
            recursive_static_to_public(src_path, dest_path)


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
    template = template.replace("{{Content}}", node)
    template = template.replace("{{Title}}", title)

    # Write the generated content to the destination file
    with open(dest_path, "w") as file:
        file.write(template)
    print(f"Generated {dest_path}")
    
    
    
    
    

















main()
