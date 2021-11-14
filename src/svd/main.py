from FungsiCompress import *

def start(filepath, percentage):
    # Untuk mendapatkan extension
    percentage_int = int(percentage)
    dot = False
    extension = ""
    for i in range(3, len(filepath)):
        if filepath[i] == '.':
            dot = True
        if dot:
            extension += filepath[i]
    if extension.lower() == ".png":
        return (Compress_png(filepath, percentage_int, extension))
    else:
        return (Compress_img(filepath, percentage_int, extension))

# DRIVER
# img, nama_file, waktu = main("../test/test4.jpg", 50)
# img.save(nama_file)
# print(waktu, "detik")
