from PIL import Image
from FungsiSVD import *
import time

def Compress_png(filepath, percentage, extension):
  start_time = time.time()
  image = Image.open(filepath).convert('RGBA')
  img_mat = np.array(image).astype(float)
  r = img_mat[:, :, 0]
  g = img_mat[:, :, 1]
  b = img_mat[:, :, 2]
  a = img_mat[:, :, 3]
  r = compress(r, percentage)
  g = compress(g, percentage)
  b = compress(b, percentage)
  img_mat[:, :, 0] = r
  img_mat[:, :, 1] = g
  img_mat[:, :, 2] = b
  img = Image.fromarray(img_mat.astype('uint8'), "RGBA")
  nama_file = "hasil" + extension
  total_waktu = time.time() - start_time
  return img, nama_file, total_waktu

def Compress_img(filepath, percentage, extension):
  start_time = time.time()
  image = Image.open(filepath).convert('RGB')
  img_mat = np.array(image).astype(float)
  r = np.array(img_mat[:, :, 0]).astype(float)
  g = np.array(img_mat[:, :, 1]).astype(float)
  b = np.array(img_mat[:, :, 2]).astype(float)
  r = compress(r, percentage)
  g = compress(g, percentage)
  b = compress(b, percentage)
  img_mat[:, :, 0] = r
  img_mat[:, :, 1] = g
  img_mat[:, :, 2] = b
  img = Image.fromarray(img_mat.astype('uint8'), "RGB")
  nama_file = "hasil" + extension
  total_waktu = time.time() - start_time
  return img, nama_file, total_waktu

# Compress_png("../test/xbox-logo-black-png-7.png", 50)
# Compress_img("../test/Logo Kirana.jpeg", 50)
