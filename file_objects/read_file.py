import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

with open('text_file.txt', 'r') as f:
    for line in f:
        print(line, end='')
