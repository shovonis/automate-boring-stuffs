#!/usr/bin/env python
import os
import pprint
import shelve

_author_ = "rifatul.islam"

current_dir = os.getcwd()
print(current_dir)

# Making dir for resource
# os.makedirs('./../resources')  # Comment out for further recreation of the dir

print("Current dir: " + os.path.abspath(current_dir))
print(os.listdir(current_dir))

# Shelve to store data on binary file

shelve_file = shelve.open("test_shelve")
cats = ['Zophie', 'Pooka', 'Simon']
shelve_file['cats'] = cats
shelve_file.close()

sheve_file2 = shelve.open("test_shelve")
type(sheve_file2)
print("The popular cats are: ", sheve_file2['cats'])

# Pretty print
cats = [{'name': 'Zophie', 'descption': 'chubby'}, {'name': 'Pooka', 'descption': 'fluffy'}]
print(pprint.pformat(cats))
