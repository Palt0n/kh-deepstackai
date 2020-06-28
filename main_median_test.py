import numpy as np
from cv2 import cv2
import requests
from PIL import Image
import os
from matplotlib import pyplot as plt
from skimage.measure import compare_ssim
import imutils

FILEPATH_MEDIAN = "background.png"
FILEPATH_MEDIAN_BLUR = "background_blur.png"

count = 0
def print_SSIM(cv2, filepath_A, filepath_B, filepath_C, filepath_new, blur_type):
    imageA = cv2.imread(filepath_A)
    imageB = cv2.imread(filepath_B)
    imageC = cv2.imread(filepath_C)
    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    grayC = cv2.cvtColor(imageC, cv2.COLOR_BGR2GRAY)
    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("{} SSIM: {}".format(blur_type, score))
    if True:
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        # loop over the contours
        global count
        for c in cnts:
            # compute the bounding box of the contour and then draw the
            # bounding box on both input images to represent where the two
            # images differ
            (x, y, w, h) = cv2.boundingRect(c)
            if w < 50 or h < 50:
                continue
            cv2.rectangle(imageA, (x, y), (x + w , y + h ), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x + w , y + h ), (0, 0, 255), 2)
            imageC_crop = imageC[y:y+h, x:x+w]
            cv2.imwrite(os.path.join("background_cat", "{}.png".format(count)), imageC_crop)
            count += 1
        # show the output images
        # cv2.imshow("Original", imageA)
        # cv2.imshow("Modified", imageB)
        # cv2.imshow("Diff", diff)
        # cv2.imshow("Thresh", thresh)
        # cv2.waitKey(0)
        cv2.imwrite(filepath_new, imageB)

list_filepaths = []
for filename in os.listdir("background"):
    filepath = os.path.join("background", filename)
    list_filepaths.append(filepath)
    # print_SSIM(cv2, FILEPATH_MEDIAN, filepath, "noBlur {}".format(filename))

list_filepaths = []
for filenameB, filenameC in zip(os.listdir("background_averaging"), os.listdir("background")):
    filepathB = os.path.join("background_averaging", filenameB)
    filepathC = os.path.join("background", filenameC)
    filepath_new = os.path.join("background_averaging_box", filenameB)
    list_filepaths.append(filepathB)
    print_SSIM(cv2, FILEPATH_MEDIAN_BLUR, filepathB, filepathC, filepath_new, "yesBlur {}".format(filename))
