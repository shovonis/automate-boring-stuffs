#!/usr/bin/env python
import os
import fnmatch
import shutil

_author = "rifatul.islam"

current_dir_files = [f for f in os.listdir(".") if os.path.isfile(f) and not f.startswith(".")]
ignore_files = ["py"]
image_extension = ["jpg", "jpeg", "png", "gif"]


def get_file_types(directory):
    """Listing all the file types in current directory"""
    type_list = []
    for file in directory:
        split_text = file.split(".")
        if len(split_text) == 2:
            file_ext = split_text[1]
            if file_ext not in ignore_files + type_list:
                type_list.append(file_ext)
        else:
            continue

    return type_list


file_types = get_file_types(current_dir_files)


"""Making directories for each file types"""
for f_type in file_types:
    if f_type in image_extension:
        os.makedirs("images", exist_ok=True)
    else:
        os.makedirs(f_type, exist_ok=True)

"""Moving files to directories"""
for f_type in file_types:
    matched_files = fnmatch.filter(current_dir_files, "*." + f_type)
    for file in matched_files:
        if f_type in image_extension:
            shutil.move(file, "images")
        else:
            shutil.move(file, f_type)
