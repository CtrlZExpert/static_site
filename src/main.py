import os
import shutil
from copydirectory import copy_directory
from generatepage import  generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory..")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("copying static files to public directory...")
    copy_directory(dir_path_static, dir_path_public)
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public )
    print("site generation complete")



main()
