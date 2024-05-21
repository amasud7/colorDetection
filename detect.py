# this file holds the function that determines the HSV boundaries for detecting specific colors
import numpy as np


# not using this function anymore, just for reference
"""
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
"""

# can add more specific colors later 
# these are hsv values [hue, saturation, value]
def red():
    lower1 = np.array([0, 250, 250], np.uint8)
    upper1 = np.array([4, 255, 255], np.uint8)
    lower2 = np.array([150, 195, 195], np.uint8)
    upper2 = np.array([180, 255, 255], np.uint8)
    return lower1, upper1, lower2, upper2

def orange():
    lower = np.array([5, 220, 220], np.uint8)
    upper = np.array([24, 255, 255], np.uint8)
    return lower, upper

def yellow():
    lower = np.array([25, 170, 170], np.uint8)
    upper = np.array([39, 255, 255], np.uint8)
    return lower, upper

def green():
    lower = np.array([40, 150, 150], np.uint8)
    upper = np.array([89, 255, 255], np.uint8)
    return lower, upper

def blue():
    lower = np.array([90, 50, 50], np.uint8)
    upper = np.array([149, 255, 255], np.uint8)
    return lower, upper

# fix white values
def white():
    lower = np.array([0, 0, 178], np.uint8)
    upper = np.array([255, 10, 255], np.uint8)
    return lower, upper







