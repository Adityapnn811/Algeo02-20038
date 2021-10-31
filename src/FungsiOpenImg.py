import cv2
import numpy as np
import FungsiEigen as eigen

def openImage(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_UNCHANGED)
    if (np.shape(img)[2] == 3):
        b = img[:, :, 0]
        g = img[:, :, 1]
        r = img[:, :, 2]
        a = None
        return b, g, r, a
    else:
        b = img[:, :, 0]
        g = img[:, :, 1]
        r = img[:, :, 2]
        a = img[:, :, 3]
        return b, g, r, a

def mergeImage(b, g, r, a=None):
    if a.all() == None:
        result = cv2.merge((b, g, r))
    else:
        result = cv2.merge((b, g, r, a))
    return result

b, g, r, a = openImage('../test/xbox-logo-png-2500.png')
# print(b, g, r, a)
cv2.imwrite('../test/test3.png', mergeImage(b, g, r, a))
# print(b)
# print(g)
# print(r)
# print(eigen.eigenValues(b))
# print(eigen.eigenValues(g))
# print(eigen.eigenValues(r))
