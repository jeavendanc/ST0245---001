import os
import numpy as np
from numpy import genfromtxt
from matplotlib import pyplot
from matplotlib.image import imsave
import cv2

class compress_csv:
    def __init__(self):
        pass
    
    def compress_file(self, img_input):

        img_data = np.genfromtxt(img_input, delimiter=',')

        img_height = len(img_data)
        img_width = len(img_data[0])

        compressed_data = np.genfromtxt(img_input, delimiter=',')

        for i in range(int(img_height / 4)):
            for j in range(int(img_width / 4)):
                square = np.reshape(img_data[i*4:(i*4)+4, j*4:(j*4)+4], (4, 4)) #Obtengo un cuadrado de 4x4 de la imagen a partir del csv
                c0, c1, c2, c3 = np.max(square), np.min(square), 0, 0 #Obtengo el valor mas grande y el mas pequeño del cuadrado

                c2 = ((2/3) * c0) + ((1/3) * c1) #La formula jaja salu2
                c3 = ((1/3) * c0) + ((2/3) * c1) #Lo de arriba x2

                #Actualizamos los valores del cuadrado
                for y in range(4):
                    for x in range(4):
                        proximityMax = abs(square[y, x] - c0)
                        proximityMin = abs(square[y, x] - c1)

                        #Si es mas cercano al valor mas pequeño seteamos c3 como su color, en caso de ser cercano al valor mas grande seteamos c2 como su valor
                        if proximityMax > proximityMin:
                            square[y, x] = int(c3)
                        else:
                            square[y, x] = int(c2)
                    #Seteamos los valores en el array (Tambien es cargado desde el archivo por si el archivo no pudo ser correctamente dividido por 4 para dejar las ultimas lineas como estaban)
                    compressed_data[i*4:(i*4)+4, j*4:(j*4)+4] = square

        #Escribimos los datos del compressed_data a un csv para ser exportado
        img_input_name = img_input.replace('./', '')
        img_input_name = img_input_name.replace('/', '')
        compressed_img = f"./Compressed-{img_input_name}"
        with open( compressed_img, "w") as file:
            for row in compressed_data:
                row_length = len(row)
                for counter, cell in enumerate(row):
                    #Si el elemento es el ultimo de la fila no agregamos una coma
                    if counter == row_length - 1:
                        file.write(f'{int(cell)}\n')
                    else:
                        file.write(f'{int(cell)},')

        self.compressed_img = compressed_img

    def show_img(self, img_input, compressed_img):
        original = genfromtxt(img_input, delimiter=',')
        imsave('original.png', original, cmap='gray')
        
        compressed = genfromtxt(compressed_img, delimiter=',')
        imsave('compressed.png', compressed, cmap='gray')

        fig = pyplot.figure(figsize=(8, 8))

        rows = 1
        columns = 2

        original_size = os.path.getsize('original.png')/1000
        compressed_size = os.path.getsize('compressed.png')/1000

        original_img = cv2.imread('original.png')
        compressed_img = cv2.imread('compressed.png')

        fig.add_subplot(rows, columns, 1)
        pyplot.imshow(original_img)
        pyplot.axis('off')
        pyplot.title("Original Image\nSize : {:.2f} kb".format(original_size))
        
        fig.add_subplot(rows, columns, 2)
        pyplot.imshow(compressed_img)
        pyplot.axis('off')
        pyplot.title("Compressed Image\nSize : {:.2f} kb".format(compressed_size))

        pyplot.show()
