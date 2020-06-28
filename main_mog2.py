import numpy as np
from cv2 import cv2
import requests
from PIL import Image
import os
from matplotlib import pyplot as plt

# cap = cv2.VideoCapture('vtest.avi')

# fgbg = cv2.createBackgroundSubtractorMOG2()

# while(1):
#     ret, frame = cap.read()

#     fgmask = fgbg.apply(frame)

#     cv2.imshow('frame',fgmask)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()


list_filepaths = []
for filename in os.listdir(r"background"):
    filepath = os.path.join(r"background", filename)
    list_filepaths.append(filepath)

if not os.path.isdir("background_blur"):
    os.mkdir("background_blur")

list_filepaths_blur = []
for filepath in list_filepaths:
    img = cv2.imread(filepath)
    filename = os.path.basename(filepath)
    blur = cv2.bilateralFilter(img,9,75,75)
    new_filepath = os.path.join(r"background_blur", filename)
    cv2.imwrite(new_filepath, blur)
    list_filepaths_blur.append(new_filepath)