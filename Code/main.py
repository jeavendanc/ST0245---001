from compress import compress_csv
from timeit import timeit
import os
from numpy import genfromtxt
import numpy as np
from matplotlib import pyplot
from matplotlib.image import imsave
import cv2
import time

already = []
path = "csv/enfermo_csv/" #Image to compress
compress_csv_dir = "./Compressed_csv/"
compress_png_dir = "./Compressed_png/"

def findimg(dire):
    for filename in os.listdir(dire):
        if filename in already:
            continue
        img_input =f"{dire}{filename}"

        already.append(filename)
        main(filename)
        show_img(filename)
        input()

def show_img(filename):

    compressed_png_name = f'{compress_png_dir}Compressed-{filename.replace(".csv",".png")}'
    original_name = path + filename 
    compressed_csv_name = compress_csv_dir + "Compressed-" + filename

    original = genfromtxt(original_name, delimiter=',')
    imsave('original.png', original, cmap='gray')
    
    compressed = genfromtxt(compressed_csv_name, delimiter=',')
    imsave(compressed_png_name, compressed, cmap='gray')

    fig = pyplot.figure(figsize=(8, 8))

    rows = 2
    columns = 2

    original_size_csv = os.path.getsize(original_name) / 1000

    original_img_png = cv2.imread('original.png')
    original_size_png = os.path.getsize('original.png') / 1000

    compressed_size_csv = os.path.getsize(compressed_csv_name)/ 1000

    compressed_img_png = cv2.imread(compressed_png_name)
    compressed_size_png = os.path.getsize(compressed_png_name)/ 1000

    fig.add_subplot(rows, columns, 1)
    pyplot.imshow(original, cmap = "gray")
    pyplot.axis('off')
    pyplot.title("Original Image CSV ({:.2f} kb)".format(original_size_csv))

    fig.add_subplot(rows, columns, 3)
    pyplot.imshow(original_img_png)
    pyplot.axis('off')
    pyplot.title("Original Image PNG({:.2f} kb)".format(original_size_png))

    fig.add_subplot(rows, columns, 2)
    pyplot.imshow(compressed, cmap="gray")
    pyplot.axis('off')
    pyplot.title("Compressed Image CSV({:.2f} kb)".format(compressed_size_csv))

    fig.add_subplot(rows, columns, 4)
    pyplot.imshow(compressed_img_png)
    pyplot.axis('off')
    pyplot.title("Compressed Image PNG({:.2f} kb)".format(compressed_size_png)) 

    pyplot.show()

def main(file):

    compress = compress_csv()
    compress.compress_file(file, path)
    
while True:
    findimg(path)
