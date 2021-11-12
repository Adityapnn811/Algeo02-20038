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
    cv2.imwrite('../test/test3.jpeg', mergeImage(b, g, r))

compress_img('../test/Logo Kirana.jpeg', 100)
