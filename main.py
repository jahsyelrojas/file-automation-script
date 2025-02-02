import os
from pathlib import Path
import shutil

os.chdir('C:/Users/Jahsyel Rojas/Documents/CIIC3015')

#rename files 
# for file in os.listdir():
#     if file == '.vscode':
#         continue
#     f=Path
#     name, ext = f.stem, f.suffix
#     splitted = name.split("_")
#     splitted = [s.strip() for s in splitted]
#     new_name = f"{splitted[0]}{ext}"
#     f.rename(new_name)

#move files to Data folder  or copy files to Data folder
# Path("Data").mkdir(exist_ok=True)
# if not os.path.exists("Data"):
#     os.mkdir("Data")

# for file in os.listdir():
#     if file == '.vscode' or file == 'Data':
#         continue
   # shutil.move(file, 'Data')
    # shutil.copy(file, 'Data')
   # shutil.copy2(file, 'Data') #copies keeping all the meta data

#os.remove('filename')
#os.rmdir('Data') #remove empty directory
#if not empty
#shutil.rmtree('Data') #remove directory with files


#organizing  desktop

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

def  is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_img(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name,ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()


os.chdir('C:/Users/Jahsyel Rojas/Desktop')

for file in os.listdir():
    if is_audio(file):
        shutil.move(file, "Users/Jahsyel Rojas/Documents/Audio")

    elif is_video(file):
        shutil.move(file, "Users/Jahsyel Rojas/Documents/Video")

    elif is_img(file):
        if is_screenshot(file):
            shutil.move(file, "Users/Jahsyel Rojas/Documents/Screenshots")
        else:
            shutil.move(file, "Users/Jahsyel Rojas/Documents/Images")

    else:
        shutil.move(file, "Users/Jahsyel Rojas/Documents/Other")
