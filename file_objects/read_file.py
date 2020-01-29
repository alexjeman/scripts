import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

with open('text_file.txt') as F:
    content = F.read()
    print(content)
    print(content[:100])
