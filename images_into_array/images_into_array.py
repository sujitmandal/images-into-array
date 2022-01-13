import os 
import cv2 
import numpy as np 
from tqdm import tqdm
from random import shuffle 

#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
This programe is create by Sujit Mandal
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
"""
#Document : https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html

#images_path = input('Enter Image Folder Path : ') #Path of the images folder
#image_height = int(input('Enter The Image Size [32, 64, 128] : ')) 
#image_width = int(input('Enter The Image Size [32, 64, 128] : '))

images_path = ('') #Path of the images folder
image_height = 32 #[32, 64, 128]
image_width = 32 #[32, 64, 128]

#NORNAL
def images(images_path, image_height, image_width):
    imges_list = []

    for image in tqdm(os.listdir(images_path)):
        path = os.path.join(images_path, image)

        image = cv2.imread(path)
        image = cv2.resize(image , (image_height, image_width))
        imges_list.append([np.array(image)])
    shuffle(imges_list)

   #Convert List Into Array
    array_image = np.array(imges_list)

    #Removed Dimention 
    images = array_image[:,0,:,:]
    return(images)

#RGB ↔ GRAY
def rgb_gray(images_path, image_height, image_width):
    imges_list = []

    for image in tqdm(os.listdir(images_path)):
        path = os.path.join(images_path, image)

        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image , (image_height, image_width))
        imges_list.append([np.array(image)])
    shuffle(imges_list)

   #Convert List Into Array
    array_image = np.array(imges_list)

    #Removed Dimention 
    images = array_image[:,0,:,:]
    return(images)


#RGB ↔ CIE L*a*b*
def rgb_lab(images_path, image_height, image_width):
    imges_list = []

    for image in tqdm(os.listdir(images_path)):
        path = os.path.join(images_path, image)

        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
        image = cv2.resize(image , (image_height, image_width))
        imges_list.append([np.array(image)])
    shuffle(imges_list)

   #Convert List Into Array
    array_image = np.array(imges_list)

    #Removed Dimention 
    images = array_image[:,0,:,:]
    return(images)


#RGB ↔ HSV
def rgb_hsv(images_path, image_height, image_width):
    imges_list = []

    for image in tqdm(os.listdir(images_path)):
        path = os.path.join(images_path, image)

        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image = cv2.resize(image , (image_height, image_width))
        imges_list.append([np.array(image)])
    shuffle(imges_list)

   #Convert List Into Array
    array_image = np.array(imges_list)

    #Removed Dimention 
    images = array_image[:,0,:,:]
    return(images)


#RGB ↔ YCrCb JPEG (or YCC)
def rgb_ycrcb(images_path, image_height, image_width):
    imges_list = []

    for image in tqdm(os.listdir(images_path)):
        path = os.path.join(images_path, image)

        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        image = cv2.resize(image , (image_height, image_width))
        imges_list.append([np.array(image)])
    shuffle(imges_list)

   #Convert List Into Array
    array_image = np.array(imges_list)

    #Removed Dimention 
    images = array_image[:,0,:,:]
    return(images)


#RGB ↔ HLS
def rgb_hls(images_path, image_height, image_width):
    imges_list = []

    for image in tqdm(os.listdir(images_path)):
        path = os.path.join(images_path, image)

        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
        image = cv2.resize(image , (image_height, image_width))
        imges_list.append([np.array(image)])
    shuffle(imges_list)

   #Convert List Into Array
    array_image = np.array(imges_list)

    #Removed Dimention 
    images = array_image[:,0,:,:]
    return(images)


#RGB ↔ CIE L*u*v*
def rgb_luv(images_path, image_height, image_width):
    imges_list = []

    for image in tqdm(os.listdir(images_path)):
        path = os.path.join(images_path, image)

        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2Luv)
        image = cv2.resize(image , (image_height, image_width))
        imges_list.append([np.array(image)])
    shuffle(imges_list)

   #Convert List Into Array
    array_image = np.array(imges_list)

    #Removed Dimention 
    images = array_image[:,0,:,:]
    return(images)


if __name__ == "__main__":
    images(images_path, image_height, image_width)
    rgb_gray(images_path, image_height, image_width)
    rgb_lab(images_path, image_height, image_width)
    rgb_hsv(images_path, image_height, image_width)
    rgb_ycrcb(images_path, image_height, image_width)
    rgb_hls(images_path, image_height, image_width)
    rgb_luv(images_path, image_height, image_width)