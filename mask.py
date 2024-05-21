import numpy as np
import cv2
from PIL import Image
import detect as dt


# bounding box (general function)
def bounding_box(frame, hsv):
    maskg = green_mask(hsv)
    mask_pilg = Image.fromarray(maskg)
    boxg = mask_pilg.getbbox() # returns (x1, y1, x2, y2) where first coordinate pair is top left corner and the other is bottom right corner of box
    if boxg:
        x1, y1, x2, y2 = boxg
        # draw rectangle with opencv and given coordinates
        # .rectangle(frame to draw on, top left corner, bottom right corner, color of box, thickness of outline)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 5)

    masko = orange_mask(hsv)
    mask_pilo = Image.fromarray(masko)
    boxo = mask_pilo.getbbox()
    if boxo:
        x1, y1, x2, y2 = boxo
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 5)

    return frame


# green mask
def green_mask(f):
    lower, upper = dt.green()
    mask = cv2.inRange(f, lower, upper)
    return mask 

# orange mask
def orange_mask(f):
    lower, upper = dt.orange()
    mask = cv2.inRange(f, lower, upper)
    return mask


