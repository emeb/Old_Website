#!/bin/python3
# script to convert all index.html in a hierarchy to markdown README
# requires mardownify - get it with pip

import os
from markdownify import markdownify


rootdir = '.'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('html'):
            fullname = os.path.join(subdir, file)
            newname = fullname.replace("html", "md")
            with open(fullname, "r") as htmlfile:
                html = htmlfile.read()
                markdown = markdownify(html, heading_style="ATX")
                with open(newname, "w") as mdfile:
                    mdfile.write(markdown)
                    print(fullname, '->', newname)


            
