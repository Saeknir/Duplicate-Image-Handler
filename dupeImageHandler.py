import matplotlib.image as mpi
import numpy as np
import cv2

#converts a color image into grayscale, then returns that image.
def grayscaleImg(file):
    img = mpi.imread(file)
    gray_img = np.dot(img[..., :3], [0.2126, 0.7152, 0.0722])
    return gray_img

#resize the image to a standard size
def resize(img):
    resized = cv2.resize(img, (64,64), interpolation=cv2.INTER_AREA)
    return resized

image = grayscaleImg("image.jpg")
image = resize(image)
cv2.imwrite("steve.jpg", image)


