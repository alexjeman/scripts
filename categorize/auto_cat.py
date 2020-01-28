import os
import shutil

dir_path = (os.path.dirname(os.path.realpath(__file__))
            + "/files_to_cat")
os.chdir(dir_path)


EXT_IMAGES = ['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png',
              '.ps', '.psd', '.svg', '.tif', '.tiff']
EXT_AUDIO = ['.aif', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma']
EXT_VIDEO = ['.3g2', '.3gp', '.avi', '.h264', '.m4v', '.mkv', '.mov', '.mp4',
             '.mpg', '.rm', '.swf', '.vob', '.wmv']
EXT_DOCUMENTS = ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt',
                 '.wks', '.wps', '.wpd', '.xlsx', '.xls', '.xlr', '.ods']
DIRS = ['images', 'audio', 'video', 'documents', 'folders', 'other']


print('Downloads folder cleanup')
print('Current directory: {}'.format(os.getcwd()))
print()


files = os.listdir()


if not os.path.isdir('./audio'):
    for d in DIRS:
        os.mkdir('./{}'.format(d))
    print('Directories created successfully')


for f in files:
    name, extension = os.path.splitext(f)

    if extension in EXT_IMAGES:
        shutil.move(f, './images/{}'.format(f))
    elif extension in EXT_AUDIO:
        shutil.move(f, './audio/{}'.format(f))
    elif extension in EXT_VIDEO:
        shutil.move(f, './video/{}'.format(f))
    elif extension in EXT_DOCUMENTS:
        shutil.move(f, './documents/{}'.format(f))
    elif os.path.isdir(name):
        if name not in DIRS:
            shutil.move(f, './folders/{}'.format(f))
    elif extension not in (EXT_DOCUMENTS + EXT_VIDEO + EXT_AUDIO + EXT_IMAGES):
        shutil.move(f, './other/{}'.format(f))


print('Files classified successfully')
