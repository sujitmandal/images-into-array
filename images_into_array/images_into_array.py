import os
import cv2
import numpy as np
from tqdm import tqdm


# GitHub: https://github.com/sujitmandal
# Author: Sujit Mandal
#
# OpenCV Color Conversion Documentation:
# https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html


# Image configuration
images_path = None  # Path of the images folder
image_height = None  # Image height: 32, 64, 128, ...
image_width = None  # Image width: 32, 64, 128, ...


def _load_images(images_path, image_height, image_width, color_conversion=None):
    """
    Load images from a folder, optionally convert color space,
    resize them, shuffle them, and return a NumPy array.

    Parameters
    ----------
    images_path : str
        Path to the image folder.

    image_height : int
        Desired image height.

    image_width : int
        Desired image width.

    color_conversion : int, optional
        OpenCV color conversion code.

    Returns
    -------
    numpy.ndarray
        Array containing processed images.
    """

    if images_path is None:
        raise ValueError("images_path cannot be None.")

    if image_height is None or image_width is None:
        raise ValueError("image_height and image_width cannot be None.")

    if not os.path.isdir(images_path):
        raise ValueError(f"Invalid image directory: {images_path}")

    if image_height <= 0 or image_width <= 0:
        raise ValueError("Image height and width must be greater than 0.")

    image_list = []

    # Supported image extensions
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}

    files = [
        file
        for file in os.listdir(images_path)
        if os.path.splitext(file)[1].lower() in valid_extensions
    ]

    for filename in tqdm(files, desc="Processing images"):
        path = os.path.join(images_path, filename)

        image = cv2.imread(path)

        # Skip images that OpenCV cannot read
        if image is None:
            continue

        # Color conversion
        if color_conversion is not None:
            image = cv2.cvtColor(image, color_conversion)

        # OpenCV expects (width, height)
        image = cv2.resize(image, (image_width, image_height))

        image_list.append(image)

    if not image_list:
        raise ValueError("No valid images found in the specified directory.")

    # Convert list directly to NumPy array
    images_array = np.array(image_list)

    # Shuffle images
    np.random.shuffle(images_array)

    return images_array


# NORMAL / BGR
def images(images_path, image_height, image_width):
    return _load_images(images_path, image_height, image_width)


# RGB → GRAY
def rgb_gray(images_path, image_height, image_width):
    return _load_images(images_path, image_height, image_width, cv2.COLOR_BGR2GRAY)


# RGB → CIE L*a*b*
def rgb_lab(images_path, image_height, image_width):
    return _load_images(images_path, image_height, image_width, cv2.COLOR_BGR2Lab)


# RGB → HSV
def rgb_hsv(images_path, image_height, image_width):
    return _load_images(images_path, image_height, image_width, cv2.COLOR_BGR2HSV)


# RGB → YCrCb
def rgb_ycrcb(images_path, image_height, image_width):
    return _load_images(images_path, image_height, image_width, cv2.COLOR_BGR2YCrCb)


# RGB → HLS
def rgb_hls(images_path, image_height, image_width):
    return _load_images(images_path, image_height, image_width, cv2.COLOR_BGR2HLS)


# RGB → CIE L*u*v*
def rgb_luv(images_path, image_height, image_width):
    return _load_images(images_path, image_height, image_width, cv2.COLOR_BGR2Luv)


if __name__ == "__main__":

    # Example configuration
    images_path = ""
    image_height = 32
    image_width = 32

    normal = images(images_path, image_height, image_width)

    gray = rgb_gray(images_path, image_height, image_width)

    lab = rgb_lab(images_path, image_height, image_width)

    hsv = rgb_hsv(images_path, image_height, image_width)

    ycrcb = rgb_ycrcb(images_path, image_height, image_width)

    hls = rgb_hls(images_path, image_height, image_width)

    luv = rgb_luv(images_path, image_height, image_width)
