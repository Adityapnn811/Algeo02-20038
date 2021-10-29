import cv2
import numpy as np

def openImage(filePath):
    img = cv2.imread(filePath)
    b = img[:,:,0]
    g = img[:,:,1]
    r = img[:,:,2]
#     print(b)
#     print(g)
#     print(r)
#
# openImage('../test/test1.png')