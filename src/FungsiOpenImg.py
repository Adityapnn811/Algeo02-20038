import cv2
import numpy as np
import FungsiEigen as eigen

def openImage(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_UNCHANGED)
    if (np.shape(img)[2] == 3):
        b = np.array(img[:, :, 0]).astype(float)
        g = np.array(img[:, :, 1]).astype(float)
        r = np.array(img[:, :, 2]).astype(float)
        a = None
        return b, g, r, a
    else:
        b = np.array(img[:, :, 0]).astype(float)
        g = np.array(img[:, :, 1]).astype(float)
        r = np.array(img[:, :, 2]).astype(float)
        a = np.array(img[:, :, 3]).astype(float)
        return b, g, r, a

def mergeImage(b, g, r, a=None):
    # if a == None:
    result = cv2.merge((b, g, r))
    # else:
    #     result = cv2.merge((b, g, r, a))
    return result

# b, g, r, a = openImage('../test/Logo Kirana.jpeg')
# print(b, g, r, a)
# cv2.imwrite('../test/test3.png', mergeImage(b, g, r, a))
# print(b)
# print(g)
# print(r)

