#!/usr/bin/env python3
import os
import re
import sys

if len(sys.argv) != 1:
    paths = sys.argv[1:]
else:
    paths = ['.']

searchString = '\[(.*?)\]'

# Generator to intersperse a delimiter into an interable
def joinit(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x

for path in paths:
    print(path)
    for item in os.listdir(path):
        if os.path.isdir(item):
            continue
        name = os.fspath(item)
        if bool(re.search(searchString,name)):
            name = name.split('.')
            newName = []
            for part in name:
                newName = newName + [re.sub(searchString,'',part).strip()]
            nameParts = joinit(newName, '.')
            name = ''
            for i in nameParts:
                name = name + i
            print(name)
        os.rename(os.path.join(path,item), os.path.join(path,name))
