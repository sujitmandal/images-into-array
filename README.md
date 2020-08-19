## Convert-Images-Into-Array:

## Convert Multiple Images into a Array and Different Color Spaces into a Array :
``
[![Downloads](https://pepy.tech/badge/images-into-array)](https://pepy.tech/project/images-into-array) [![Downloads](https://pepy.tech/badge/images-into-array/month)](https://pepy.tech/project/images-into-array/month) [![Downloads](https://pepy.tech/badge/images-into-array/week)](https://pepy.tech/project/images-into-array/week)
``
## PyPI package : 
```
pip install images-into-array
```

[Package LInk](https://pypi.org/project/images-into-array/)

## Convert-Images-Into-Array:
Convert Multiple Images into a Array and Different Color Spaces into a Array :
-------------------------------------------------------------------------------
This package fuction requres three argument one is path of the images folder and other is image_height and image_width.

OpenCV Document :
-----------------
[OpenCV Document](https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html)

## How to import the module:

```
images_path = ('')

image_height = Enter The Image Size [32, 64, 128]

image_width = Enter The Image Size [32, 64, 128]
```
##NORMAL :
```
from images_into_array.images_into_array import images

array = images(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ GRAY :
```
from images_into_array.images_into_array import rgb_gray

gray = rgb_gray(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ CIE L*a*b* :
```
from images_into_array.images_into_array import rgb_lab

lav = rgb_lab(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ HLS :
```
from images_into_array.images_into_array import rgb_hls

hls = rgb_hls(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ CIE L*u*v* :
```
from images_into_array.images_into_array import rgb_luv

luv = rgb_luv(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ HSV :
```
from images_into_array.images_into_array import rgb_hsv

hsv = rgb_hsv(images_path, image_height, image_width)

print(array.shape)
```
## RGB ↔ YCrCb JPEG (or YCC) :
```
from images_into_array.images_into_array import rgb_ycrcb

ycrcb = rgb_ycrcb(images_path, image_height, image_width)

print(array.shape)
```

## Requirement’s:
```
• Python 

• Anaconda

• Visual Studio Code
```
## LINK’S:
• [Python Download](https://www.python.org/downloads/)

• [Anaconda Download](https://www.anaconda.com/downloads)

• [Visual Studio Download](https://code.visualstudio.com/Download)

## Linux:

## How to install Anaconda In Linux | Create Environment | Install TensorFlow | Opencv library |
 [![How to install | Python | | Anaconda | | Opencv library |](https://yt-embed.herokuapp.com/embed?v=Mfbrxy8gK6A)](https://www.youtube.com/watch?v=Mfbrxy8gK6A "How to install Anaconda In Linux | Create Environment | Install TensorFlow | Opencv library |")

##  Windows:

## How to install | Python | | Anaconda | | Opencv library |
 [![How to install | Python | | Anaconda | | Opencv library |](https://yt-embed.herokuapp.com/embed?v=eVV3byQlYvA)](https://www.youtube.com/watch?v=eVV3byQlYvA "How to install | Python | | Anaconda | | Opencv library |")

## Installing the required package’s:
```
• conda install -c conda-forge opencv=4.2.0

• pip install shuffle

• pip install numpy

• pip install tqdm
```
License:
--------
MIT Licensed

Author:
-------
Sujit Mandal

[LinkedIn](https://www.linkedin.com/in/sujit-mandal-91215013a/)

[Facebook](https://www.facebook.com/sujit.mandal.33671748)

[Twitter](https://twitter.com/mandalsujit37)
