from PIL import Image
from numpy import asarray
from matplotlib import pyplot as plt

def openImg(filename):
  image = Image.open(filename)
  data = asarray(image)

  plt.imshow(np.array(data), interpolation='none')
  plt.show()