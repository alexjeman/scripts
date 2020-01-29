import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

with open('text_file_w.txt', "a+") as newf:
    newf.write(f"item\n")

    # Move cursor to line 0
    newf.seek(0)
    print(newf.read())
    newf.close()

with open("text_file.txt") as file:
    contents = file.read()
with open("text_file_s.txt", "a+") as newf:
    newf.write(contents[:90])
