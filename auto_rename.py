"""
Rename Sun-Wallpapers-34-1920-x-1080.jpg to 01-SunWallpapers.jpg
"""
import os

os.chdir('/home/alex/Pictures')

i = 0
for f in os.listdir():
    i += 1
    f_name, f_ext = os.path.splitext(f)

    f_title1, f_title2, _, _, _, _ = f_name.split('-')

    new_name = f"{str(i).zfill(2)}-{f_title1}{f_title2}{f_ext}"

    os.rename(f, new_name)
