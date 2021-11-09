from FungsiSVD import *
from FungsiOpenImg import *

def compress_img(filepath, percentage):
    b, g, r, a = openImage(filepath)
    b = compress(b, percentage)
    g = compress(g, percentage)
    r = compress(r, percentage)
    if a.all() != None:
        a = compress(a, percentage)
    cv2.imwrite('../test/test3.png', mergeImage(b, g, r, a))

compress_img('../test/test2.png', 50)
