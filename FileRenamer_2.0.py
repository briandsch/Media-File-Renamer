import os
from exif import Image
from datetime import datetime


while True:
    path = input("Please enter the folder's path: ")
    # path = "C:\\Users\\Brian\\Videos\\Pictures Nikon"
    start = datetime.now()
    pathList = []

    while True:
        for dirs in os.walk(path):
            pathList.append(dirs[0] + "\\")
        if pathList == []:
            path = input("The path appears to be incorrect, please try again: ")
            continue
        else:
            break

    for i in pathList:
        for filename in os.listdir(i):
            if filename[0:2] == "20" and len(filename) == 23: # Not perfect, but probably good enough.
                print(f"{filename} does not need to be renamed.")
                continue
            if filename[filename.rfind("."):].lower() in [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".tif", ".psd", ".bmp"]:         
                try:
                    with open(i + filename, "rb") as currFile:
                        currImage = Image(currFile)
                        dttImage = datetime.strptime(currImage.datetime_original, "%Y:%m:%d %H:%M:%S")
                        nameFile = datetime.strftime(dttImage, "%Y-%m-%d_%H.%M.%S")
                    srcFile = i + filename
                    destFile = i + nameFile + filename[filename.rfind("."):]
                    os.rename(srcFile, destFile)
                    print(f"{filename} has been renamed.")
                except:
                    print(f"{filename} could not be renamed.")
                    continue
            elif filename[filename.rfind("."):].lower() in [".mp4", ".mov", ".avi", ".wmv", ".flv"]:
                try:
                    ts = os.path.getmtime(i + filename)
                    dt = datetime.fromtimestamp(ts)
                    nameFile = datetime.strftime(dt, "%Y-%m-%d_%H.%M.%S")
                    destFile = i + nameFile + filename[filename.rfind("."):]
                    os.rename(i + filename, destFile)
                    print(f"{filename} has been renamed.")
                except:
                    print(f"{filename} could not be renamed.")
                    continue    
            else:
                print(f"{filename} is not an image.")
                continue

    end = datetime.now()

    print("All done. Elapsed time:", end - start)
    

