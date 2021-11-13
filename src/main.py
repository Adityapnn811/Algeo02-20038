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
        return Compress_png(filepath, percentage, extension)
    else:
        return Compress_img(filepath, percentage, extension)

# DRIVER
# img, nama_file, waktu = main("../test/test4.jpg", 50)
# img.save(nama_file)
# print(waktu, "detik")
