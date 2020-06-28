import numpy as np
from cv2 import cv2
import requests
from PIL import Image
import os
from matplotlib import pyplot as plt
from skimage.measure import compare_ssim

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

POS_A = 0
POS_B = 1

def print_SSIM(cv2, filepath_A, filepath_B, blur_type):
    imageA = cv2.imread(filepath_A)
    imageB = cv2.imread(filepath_B)
    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("{} SSIM: {}".format(blur_type, score))

list_filepaths = []
for filename in os.listdir(r"background"):
    filepath = os.path.join(r"background", filename)
    list_filepaths.append(filepath)
print_SSIM(cv2, list_filepaths[POS_A], list_filepaths[POS_B], "noBlur")

# averaging
DIRNAME_BLUR = "background_averaging"
list_filepaths_blur = []
if not os.path.isdir(DIRNAME_BLUR):
    os.mkdir(DIRNAME_BLUR)
for filepath in list_filepaths:
    img = cv2.imread(filepath)
    filename = os.path.basename(filepath)
    blur = cv2.blur(img,(10,10))
    new_filepath = os.path.join(DIRNAME_BLUR, filename)
    cv2.imwrite(new_filepath, blur)
    list_filepaths_blur.append(new_filepath)
print_SSIM(cv2, list_filepaths_blur[POS_A], list_filepaths_blur[POS_B], DIRNAME_BLUR)

# GaussianBlur
DIRNAME_BLUR = "background_GaussianBlur"
list_filepaths_blur = []
if not os.path.isdir(DIRNAME_BLUR):
    os.mkdir(DIRNAME_BLUR)
for filepath in list_filepaths:
    img = cv2.imread(filepath)
    filename = os.path.basename(filepath)
    blur = cv2.GaussianBlur(img,(5,5),0)
    new_filepath = os.path.join(DIRNAME_BLUR, filename)
    cv2.imwrite(new_filepath, blur)
    list_filepaths_blur.append(new_filepath)
print_SSIM(cv2, list_filepaths_blur[POS_A], list_filepaths_blur[POS_B], DIRNAME_BLUR)

# medianBlur
DIRNAME_BLUR = "background_medianBlur"
list_filepaths_blur = []
if not os.path.isdir(DIRNAME_BLUR):
    os.mkdir(DIRNAME_BLUR)
for filepath in list_filepaths:
    img = cv2.imread(filepath)
    filename = os.path.basename(filepath)
    blur = cv2.medianBlur(img,5)
    new_filepath = os.path.join(DIRNAME_BLUR, filename)
    cv2.imwrite(new_filepath, blur)
    list_filepaths_blur.append(new_filepath)
print_SSIM(cv2, list_filepaths_blur[POS_A], list_filepaths_blur[POS_B], DIRNAME_BLUR)

# bilateralFilter
DIRNAME_BLUR = "background_bilateralFilter"
list_filepaths_blur = []
if not os.path.isdir(DIRNAME_BLUR):
    os.mkdir(DIRNAME_BLUR)
for filepath in list_filepaths:
    img = cv2.imread(filepath)
    filename = os.path.basename(filepath)
    blur = cv2.bilateralFilter(img,9,75,75)
    new_filepath = os.path.join(DIRNAME_BLUR, filename)
    cv2.imwrite(new_filepath, blur)
    list_filepaths_blur.append(new_filepath)
print_SSIM(cv2, list_filepaths_blur[POS_A], list_filepaths_blur[POS_B], DIRNAME_BLUR)