"""
source env/Scripts/activate
"""
import numpy as np
import imageio
import matplotlib.pyplot as plt
import os
from cv2 import cv2

list_filepaths = []
DIRNAME = "background"
for filename in os.listdir(DIRNAME):
    filepath = os.path.join(DIRNAME, filename)
    list_filepaths.append(filepath)

list_images = []
for filepath in list_filepaths:
    image = imageio.imread(filepath, as_gray=True)
    list_images.append(image)

list_images = list_images
print(list_images[0].shape) # (100, 100)

images_stack = np.vstack([image.reshape(1,image.shape[0] * image.shape[1]) for image in list_images])
print(images_stack.shape) # (5, 10000)

median = np.median(images_stack, axis=0).reshape(1520, 2688)
filepath_new = "{}.png".format(DIRNAME)
imageio.imwrite(filepath_new, median.astype(np.uint8))

filepath_new_blur = "{}_blur.png".format(DIRNAME)
img = cv2.imread(filepath_new)
blur = cv2.blur(img,(10,10))
cv2.imwrite(filepath_new_blur, blur)