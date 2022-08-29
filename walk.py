#!/bin/python3
# script to convert all index.html in a hierarchy to markdown README
# requires mardownify - get it with pip

import os
from markdownify import markdownify


rootdir = 'github'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file  == 'index.html':
            fullname = os.path.join(subdir, file)
            with open(fullname, "r") as htmlfile:
                html = htmlfile.read()
                markdown = markdownify(html, heading_style="ATX")
                newname = os.path.join(subdir, 'README.md')
                with open(newname, "w") as mdfile:
                    mdfile.write(markdown)
                    print(fullname, '->', newname)


            
