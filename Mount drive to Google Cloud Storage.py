import numpy as np
import os
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

# Array of Folders
folderData = "/content/drive/MyDrive/Dataset/"
folderArray = np.array(os.listdir(folderData))

base_gcs_path = "gs://image-products-kirat/"

data_array = []

def main():

data = "/content/drive/MyDrive/Dataset/"
for currentFolder in folderArray:
  fileData = data + currentFolder + "/"
  fileArray = np.array(os.listdir(fileData))
  for currentFile in fileArray:
    if (".jpeg" or ".jpg" or ".png") not in currentFile: 
      continue # don't include non-photos
    data_array.append((base_gcs_path + currentFolder + '/' + currentFile , currentFolder))

if __name__ == '__main__':
    main()

dataframe = pd.DataFrame(data_array)
dataframe
