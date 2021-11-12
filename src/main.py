from FungsiSVD import *
from FungsiOpenImg import *
import time

def compress_img(filepath, percentage):
    start_time = time.time()
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
    print("--- %s seconds ---" % (time.time() - start_time))

compress_img('../test/test5.jpg', 50)
