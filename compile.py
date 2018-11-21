import os
import sys
import re

dirt = "templates/"


def readTemplate(filename):
    with open(dirt+filename, "r") as fin:
        content = fin.read()
    return content


def writeOut(content, filename):
    with open(filename, "w") as fout:
        fout.write(content)


pattern = re.compile(r'{%.*?%}')
for filename in os.listdir(dirt):
    if len(filename) <= 2 or filename[:2] != "__":
        continue
    content = readTemplate(filename)
    for item in pattern.findall(content):
        replacer = readTemplate(item[2:-2].strip())
        content = content.replace(item, replacer, 1)
    writeOut(content, filename[2:])
