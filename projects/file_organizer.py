#!/usr/bin/env python
import os
import fnmatch
import shutil

_author = "rifatul.islam"

current_dir_files = [f for f in os.listdir(".") if os.path.isfile(f) and not f.startswith(".")]
ignore_files = ["py"]


def get_file_types(directory):
    """Listing all the file types in current directory"""
    file_types = []
    for file in directory:
        file_ext = file.split(".")[1]
        if file_ext not in ignore_files + file_types:
            file_types.append(file_ext)

    return file_types


file_types = get_file_types(current_dir_files)


"""Making directories for each file types"""
for f_type in file_types:
    os.makedirs(f_type, exist_ok=True)

"""Moving files to directories"""
for f_type in file_types:
    matched_files = fnmatch.filter(current_dir_files, "*." + f_type)
    for file in matched_files:
        shutil.move(file, f_type)
