'''
Agosh Saini - as7saini@uwaterloo.ca

Objective - Creating a video from a set of photos in a folder.
  
'''

#Importing relevent dependecies 
import cv2 
import glob
import os

#Empty Array for storing images and size
img_array = []
    
#Pulls imgaes from the folders, and addes to empty array img_array
for filename in sorted(glob.glob('data/*.png'), key=os.path.getmtime):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
       
#Object that puts all photos together
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
video_out = cv2.VideoWriter('output.mp4',fourcc, 30, size)
        
#Putting photos together
for i in range(len(img_array)):
    video_out.write(img_array[i])
        
#Releasing the created Video
video_out.release()
