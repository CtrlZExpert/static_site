import os
import shutil

def copy_directory(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        dest_path =  os.path.join(destination, filename)
        print(f"* {source} -> {destination}")
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_directory(source_path, dest_path)
