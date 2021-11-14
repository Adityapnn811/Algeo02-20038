from PIL import Image
from FungsiSVD import *
import time

def Compress_png(filepath, percentage, extension):
  start_time = time.time()
  image = Image.open(filepath).convert('RGBA')
  img_mat = np.array(image).astype(float)
  baris = np.shape(img_mat)[0]
  kolom = np.shape(img_mat)[1]
  rank = int((percentage / 100) * min(baris, kolom))
  pixel_diff = ((baris * rank) + rank + (rank * kolom)) / (baris * kolom) * 100
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
  img.save('static/image/hasil-Extension' + extension)
  nama_file = "hasil-Extension" + extension
  total_waktu = time.time() - start_time
  string_total_waktu = str(total_waktu)
  return (nama_file, string_total_waktu, pixel_diff)

def Compress_img(filepath, percentage, extension):
  start_time = time.time()
  image = Image.open(filepath).convert('RGB')
  img_mat = np.array(image).astype(float)
  baris = np.shape(img_mat)[0]
  kolom = np.shape(img_mat)[1]
  rank = int((percentage/100) * min(baris, kolom))
  pixel_diff = ((baris*rank) + rank + (rank*kolom))/(baris*kolom) * 100
  # r = np.array(img_mat[:, :, 0]).astype(float)
  # g = np.array(img_mat[:, :, 1]).astype(float)
  # b = np.array(img_mat[:, :, 2]).astype(float)
  # r = compress(r, percentage)
  # g = compress(g, percentage)
  # b = compress(b, percentage)
  # img_mat[:, :, 0] = r
  # img_mat[:, :, 1] = g
  # img_mat[:, :, 2] = b
  # img = Image.fromarray(img_mat.astype('uint8'), "RGB")
  # img.save('static/image/hasil-Extension' + extension)
  nama_file = "hasil-Extension" + extension
  total_waktu = time.time() - start_time
  string_total_waktu = str(total_waktu)
  return (nama_file, string_total_waktu, pixel_diff)

# Compress_img("../temp/temp.jpg", 10, ".jpg")
# Compress_img("../test/Logo Kirana.jpeg", 50)
