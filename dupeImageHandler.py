import matplotlib.image as mpi
import numpy as np

def grayscaleImg(file):
    img = mpi.imread(file)
    gray_img = np.dot(img[..., :3], [0.2126, 0.7152, 0.0722])
    mpi.imsave("steve.jpg", gray_img, cmap="gray")

grayscaleImg("image.jpg")
