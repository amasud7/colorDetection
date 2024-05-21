import numpy as np
import cv2
from PIL import Image
import detect as dt


# bounding box (general function how do i simplify more so i dont have if statement for each color?)
def bounding_box(frame, hsv):

    # green
    maskg = green_mask(hsv)
    mask_pilg = Image.fromarray(maskg)
    boxg = mask_pilg.getbbox() # returns (x1, y1, x2, y2) where first coordinate pair is top left corner and the other is bottom right corner of box
    if boxg:
        x1, y1, x2, y2 = boxg
        # .putText(frame, text, location font, scaling factor, color of text, thickness in px)
        cv2.putText(frame, 'Green', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)

        # draw rectangle with opencv and given coordinates
        # .rectangle(frame to draw on, top left corner, bottom right corner, color of box, thickness of outline)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # orange
    masko = orange_mask(hsv)
    mask_pilo = Image.fromarray(masko)
    boxo = mask_pilo.getbbox()
    if boxo:
        x1, y1, x2, y2 = boxo
        cv2.putText(frame, 'Orange', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 165, 255), 5)

    # blue
    maskb = blue_mask(hsv)
    mask_pilb = Image.fromarray(maskb)
    boxb = mask_pilb.getbbox()
    if boxb:
        x1, y1, x2, y2 = boxb
        cv2.putText(frame, 'Blue', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 5)


    # yellow
    masky = yellow_mask(hsv)
    mask_pily = Image.fromarray(masky)
    boxy = mask_pily.getbbox()
    if boxy:
        x1, y1, x2, y2 = boxy
        cv2.putText(frame, 'Yellow', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 5)


    # red
    maskr = red_mask(hsv)
    mask_pilr = Image.fromarray(maskr)
    boxr = mask_pilr.getbbox()
    if boxr:
        x1, y1, x2, y2 = boxr
        cv2.putText(frame, 'Red', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)


    # white
    maskw = white_mask(hsv)
    mask_pilw = Image.fromarray(maskw)
    boxw = mask_pilw.getbbox()
    if boxw:
        x1, y1, x2, y2 = boxw
        cv2.putText(frame, 'White', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 5)

    

# implement color borders depending on which color it detects, labels also maybe?
# fix yellow and orange range

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

# yellow mask
def yellow_mask(f):
    lower, upper = dt.yellow()
    mask = cv2.inRange(f, lower, upper)
    return mask

# blue mask
def blue_mask(f):
    lower, upper = dt.blue()
    mask = cv2.inRange(f, lower, upper)
    return mask

def red_mask(f):
    lower1, upper1, lower2, upper2 = dt.red()
    mask1 = cv2.inRange(f, lower1, upper1)
    mask2 = cv2.inRange(f, lower2, upper2)
    mask = mask1 + mask2
    return mask

def white_mask(f):
    lower, upper = dt.white()
    mask = cv2.inRange(f, lower, upper)
    return mask

