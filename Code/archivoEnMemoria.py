import glob
import numpy as np


# Reads the paths of all csv files from a folder

files = glob.glob("./csv/sano_csv/*.csv")
folderFiles = {}

# Stores all csv files in a dictionary as an array

i= 0
for myFile in files:
    image_data = np.genfromtxt(myFile, delimiter=",").astype(int)
    key = files[i]
    folderFiles[key] = image_data
    i += 1

# Prints the dictionary with the paths and arrays of each image

print(folderFiles)
