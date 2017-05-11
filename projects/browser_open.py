#!/usr/bin/env python
import json
import os
import webbrowser

_author_ = "rifatul.islam"

os.chdir(os.path.expanduser("~") + "/.config/google-chrome/Default/")

with open("Bookmarks") as json_file:
    json_data = json.load(json_file)

bookmark_bars = json_data["roots"]["bookmark_bar"]["children"]

for link in bookmark_bars:
    webbrowser.open_new(link["url"])
