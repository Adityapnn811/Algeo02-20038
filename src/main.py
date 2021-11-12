from FungsiSVD import *
from FungsiOpenImg import *

def compress_img(filepath, percentage):
    b, g, r, a = openImage(filepath)
    b = compress(b, percentage)
    g = compress(g, percentage)
    r = compress(r, percentage)
    # if a.all() != None:
    #     a = compress(a, percentage)
    # elif a != None:
    #     a = compress(a, percentage)
    dot = False
    extension = ""
    for i in range(3, len(filepath)):
        if filepath[i] == '.':
            dot = True
        if dot:
            extension += filepath[i]
    cv2.imwrite('../test/hasil' + extension, mergeImage(b, g, r))

compress_img('../test/test4.jpg', 50)
