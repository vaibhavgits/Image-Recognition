'''This python code will rename the files present in your folder with the folder's name. So if the Folder's name is "Sample" then the files will be ranmaed to "Sample1.jpeg", "Sample2.jpeg" '''

'''Code to mount the drive. Mount means to make a group of files in a 
file system structure accessible to a user or user group.'''
from google.colab import drive
from google.colab import files
drive.mount('/content/drive')

''' Mount the Dataset folder to the drive '''
import os
import numpy as np
//data is the path of main folder which contains all the subfolders with images.
data = " " 


'''folderArray is the array of all the folders in the Dataset.
folder is the name of thermoplastic product and it contains images of 
thermoplastic product e.g. ['Demo' 'Sample'] '''
folderArray = np.array(os.listdir(data))

def main():

#1st-for-loop to traverse folders of the Dataset Folder
  '''2nd-for-loop to traverse files inside the nth folder of the 
  Dataset Folder'''

  for currentFolder in folderArray:
    data2 = data + currentFolder + "/"
    i = 1
    fileArray = np.array(os.listdir(data2))
    for currentFile in fileArray:
      src = data2+ currentFile
      dst = data2 + currentFolder +str(i)+ ".jpeg"

      '''os.rename(source, dest)- 
      Rename source(path) to destination(path)'''
      os.rename(src, dst)
      i += 1

if __name__ == '__main__':
    main()
