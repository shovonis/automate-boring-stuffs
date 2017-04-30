#!/usr/bin/env python
import shutil
import send2trash
import os

_author_ = "rifatul.islam"

os.makedirs("tmp", exist_ok=True)

for fileName in os.listdir():
    print(fileName)
    if fileName.endswith('.txt'):
        os.unlink(fileName)

send2trash.send2trash("tmp/test.txt")
