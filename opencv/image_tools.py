# Python 3.8
# file: image_tools.py
# requirements: apt-package (python3-opencv) or pip-package (opencv-python). Warn: conflict.
# author: steve.jeong Python 3.8

import cv2
import numpy as np

def read_images():
  # read image
  orig_img = cv2.imread('Lenna.png', cv2.IMREAD_COLOR)
  # read image with gray scale
  gray_img = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
  # show images
  cv2.imshow('origin', orig_img)
  cv2.imshow('gray', gray_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def save_images():
  # read original image
  orig_img = cv2.imread('Lenna.png')
  # edit image
  gray_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
  rgb_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
  hsv_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
  yuv_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2YUV)
  resized_img = cv2.resize(orig_img, (224, 224))
  # save images
  cv2.imwrite('gray.png', gray_img)
  cv2.imwrite('rgb.png', rgb_img)
  cv2.imwrite('hsv.png', hsv_img)
  cv2.imwrite('yuv.png', yuv_img)
  cv2.imwrite('resized.png', resized_img)

def filtering_images():
  orig_img = cv2.imread('Lenna.png')
  # convolution
  kernel = np.ones((5,5), np.float32)/25
  conv_img = cv2.filter2D(orig_img, -1, kernel)
  # bluring
  blur_img = cv2.blur(orig_img, (5,5))
  gaub_img = cv2.GaussianBlur(orig_img, (5,5), 0)
  medb_img = cv2.medianBlur(orig_img, 5)
  bilf_img = cv2.bilateralFilter(orig_img, 9, 75, 75)
  # show images
  cv2.imshow('convolution', conv_img)
  cv2.imshow('blur', blur_img)
  cv2.imshow('GaussianBlur', gaub_img)
  cv2.imshow('medianBlur', medb_img)
  cv2.imshow('bilateralFilter', bilf_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def edge_detect_images():
  orig_img = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
  min_thres = 50
  max_thres = 100
  canny_img = cv2.Canny(orig_img, min_thres, max_thres)
  # show images
  cv2.imshow('canny', canny_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == '__main__':
  run = edge_detect_images()

# vim: set ft=python ts=2 sw=2 sts=2 et
