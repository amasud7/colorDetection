# this file holds the function that determines the HSV boundaries for detecting specific colors
import numpy as np
import cv2

# pass in array of bgr values for specific color
def find_hsv(color):
    # limiting numbers to 0 - 255 using uint8 and adding [[]] to make 3x3 numpy array (this is needed for cvtColor() to convert to HSV)
    c = np.uint8([[color]])


    # converting passed in bgr colorspace to hsv
    hsv_val = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    # finding upper and lower limits of colors
    # hsv_val[0][0][0] is the first value of (h, s, v) --> hue
    # 100 and 255 for saturation and value is arbitrary just to create a normal range where most colors appear
    lower_lim = np.array([hsv_val[0][0][0] - 10, 100, 100], np.uint8)
    upper_lim = np.array([hsv_val[0][0][0] + 10, 255, 255], np.uint8)

    return lower_lim, upper_lim




