#!/usr/bin/env python3
import os
import re
import sys

if len(sys.argv) != 1:
    paths = sys.argv[1:]
else:
    paths = ['.']

searchString = '\(.*?\)|\[.*?\]'

# Generator to intersperse a delimiter into an interable
def joinit(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x

for path in paths:
    print(os.path.abspath(path))
    for item in os.listdir(path):
        if os.path.isdir(item):
            continue
        name = os.fspath(item)
        oldname = os.fspath(item)
        if bool(re.search(searchString,name)):
            # Strip regex matches and split into list of parts
            name = re.sub(searchString,'',name).split('.')
            newNameList = []
            # Accumulate new list with whitespace stripped
            for part in name:
                # newNameList
                newNameList = newNameList + [part.strip()]
            # Add back all of the '.' lost in filename during split as list elements
            newNameList = joinit(newNameList, '.')
            name = ''
            for part in newNameList:
                 name = name + part
            print(oldname + ' -> ' + name)
        os.rename(os.path.join(path,item), os.path.join(path,name))
        
