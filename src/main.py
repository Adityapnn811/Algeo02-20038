from FungsiCompress import *

def main(filepath, percentage):
    # Untuk mendapatkan extension
    dot = False
    extension = ""
    for i in range(3, len(filepath)):
        if filepath[i] == '.':
            dot = True
        if dot:
            extension += filepath[i]
    if extension.lower() == ".png":
        Compress_png(filepath, percentage, extension)
    else:
        Compress_img(filepath, percentage, extension)

main("../test/test4.jpg", 50)
