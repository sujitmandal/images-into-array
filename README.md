# images-into-array

[![Build Status](https://travis-ci.org/sujitmandal/images-into-array.svg?branch=master)](https://travis-ci.org/sujitmandal/images-into-array) [![GitHub license](https://img.shields.io/github/license/sujitmandal/images-into-array)](https://github.com/sujitmandal/images-into-array/blob/master/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/images-into-array) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/images-into-array) ![PyPI](https://img.shields.io/pypi/v/images-into-array) [![Conda Version](https://img.shields.io/conda/vn/conda-forge/images-into-array.svg)](https://anaconda.org/conda-forge/images-into-array) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/images-into-array/badges/version.svg)](https://anaconda.org/conda-forge/images-into-array) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/images-into-array/badges/installer/conda.svg)](https://conda.anaconda.org/conda-forge) [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/images-into-array.svg)](https://anaconda.org/conda-forge/images-into-array) [![Conda Recipe](https://img.shields.io/badge/recipe-images--into--array-green.svg)](https://anaconda.org/conda-forge/images-into-array) ![](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/images-into-array-feedstock?branchName=main)

[![Downloads](https://pepy.tech/badge/images-into-array)](https://pepy.tech/project/images-into-array) 

`images-into-array` is a Python package for loading multiple images from
a directory, resizing them to a common size, optionally converting them
into different OpenCV color spaces, and returning them as NumPy arrays.

The package was originally developed as part of research work on masked
face detection and employee access control.

## Features

-   Load multiple images from a directory.
-   Resize images to a specified height and width.
-   Return images as NumPy arrays.
-   Support grayscale and multiple OpenCV color spaces.
-   Preserve the original public function names for backwards
    compatibility.
-   Simple API suitable for computer-vision and machine-learning
    workflows.

## Installation

### PyPI

``` bash
pip install images-into-array
```

### Conda

``` bash
conda install -c conda-forge images-into-array
```

[Package Link](https://pypi.org/project/images-into-array/)


[Conda Package Link](https://anaconda.org/conda-forge/images-into-array)

[images-into-array-feedstock](https://github.com/conda-forge/images-into-array-feedstock)


## Usage

The image directory and image dimensions should be supplied to the
functions.

``` python
from images_into_array import images

images_path = "/path/to/images"
image_height = 32
image_width = 32

image_array = images(images_path, image_height, image_width)

print(image_array.shape)
```

For example, if the directory contains 100 RGB/BGR images and the
requested size is `32 x 32`, the returned array will normally have a
shape similar to:

``` text
(100, 32, 32, 3)
```

For grayscale images:

``` text
(100, 32, 32)
```

> Note: OpenCV reads color images in **BGR** order by default. The
> package therefore uses OpenCV's BGR-based color conversion operations.

## Supported Functions

  Function        OpenCV conversion   Description
  --------------- ------------------- -----------------------------
  `images()`      None                Load normal color images
  `rgb_gray()`    `BGR2GRAY`          Convert images to grayscale
  `rgb_lab()`     `BGR2Lab`           Convert images to Lab
  `rgb_hsv()`     `BGR2HSV`           Convert images to HSV
  `rgb_ycrcb()`   `BGR2YCrCb`         Convert images to YCrCb
  `rgb_hls()`     `BGR2HLS`           Convert images to HLS
  `rgb_luv()`     `BGR2Luv`           Convert images to Luv

The `rgb_*` function names are retained for compatibility with earlier
versions of the package.

## Examples

### Normal Images

``` python
from images_into_array import images

images_path = "/path/to/images"
image_height = 32
image_width = 32

data = images(images_path, image_height, image_width)
```

### Grayscale

``` python
from images_into_array import rgb_gray

data = rgb_gray(images_path, image_height, image_width)
```

### Lab

``` python
from images_into_array import rgb_lab

data = rgb_lab(images_path, image_height, image_width)
```

### HSV

``` python
from images_into_array import rgb_hsv

data = rgb_hsv(images_path, image_height, image_width)
```

### YCrCb

``` python
from images_into_array import rgb_ycrcb

data = rgb_ycrcb(images_path, image_height, image_width)
```

### HLS

``` python
from images_into_array import rgb_hls

data = rgb_hls(images_path, image_height, image_width)
```

### Luv

``` python
from images_into_array import rgb_luv

data = rgb_luv(images_path, image_height, image_width)
```

## Requirements

The package uses:

-   Python
-   NumPy
-   OpenCV
-   tqdm

Install the main dependencies with:

``` bash
pip install numpy opencv-python tqdm
```

The package does **not** require the third-party `shuffle` package.
Python provides `random.shuffle` as part of the standard library.

## Important Notes

### Image dimensions

OpenCV's `cv2.resize()` expects the size in:

``` python
(width, height)
```

Therefore, even though the API accepts:

``` python
image_height
image_width
```

the resize operation should use:

``` python
cv2.resize(image, (image_width, image_height))
```

### Invalid or unreadable images

If an image cannot be read by OpenCV, `cv2.imread()` may return `None`.
Production code should handle such files rather than attempting to
resize them.

### Reproducibility

If the image order is shuffled for machine-learning experiments,
consider using a fixed random seed when reproducible experiments are
required.

## Research

This package was developed in connection with research on masked face
detection and selected employee access to workplaces.

### Published Research

**Mandal, S., Saha, M. & Chatterji, B.N.**\
*Masked Face Detection and Selected Employee Access to Workplaces: A
Step Towards Coronavirus Prevention.*

Journal of The Institution of Engineers (India): Series B, **104**,
1353--1368 (2023).

DOI: https://doi.org/10.1007/s40031-023-00945-5

The research presents a CCTV-based approach for detecting masked faces
and identifying selected employees, using a two-tier convolutional
neural network.

## Source Code

GitHub repository:

https://github.com/sujitmandal/images-into-array

PyPI:

https://pypi.org/project/images-into-array/

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

## Author

**Sujit Mandal**

GitHub: https://github.com/sujitmandal

## Citation

If you use this package or the associated research in academic work,
please cite the published paper:

``` text
Mandal, S., Saha, M. & Chatterji, B.N. Masked Face Detection and Selected Employee Access to Workplaces: A Step Towards Coronavirus Prevention. Journal of The Institution of Engineers (India): Series B 104, 1353–1368 (2023). https://doi.org/10.1007/s40031-023-00945-5
```