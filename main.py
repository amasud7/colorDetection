# main function runs everything together for program
import numpy as np
import cv2
from PIL import Image
from detect import find_hsv # import  custom function to find hsv values

# webcam function from open cv, creates cam object which can then be used to feed frames
cam = cv2.VideoCapture(0)

# infinite loop to get continious feed of frames
color = [0, 0, 255]
while True:
    # read() returns boolean value stored in cap that says whether frames are being captured or not
    # returns the actual frame and stores in frame
    cap, frame = cam.read()

    # .imshow(name of window, frame object to be shown)
    #cv2.imshow('Webcam', frame)

    # convert image to hsv
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # for now we are only implementing detection of one color
    lower, upper = find_hsv(color)
    mask = cv2.inRange(hsv_frame, lower, upper)

    # Pillow library to get box
    mask_pil = Image.fromarray(mask)
    box = mask_pil.getbbox() # returns (x1, y1, x2, y2) where first coordinate pair is top left corner and the other is bottom right corner of box

    if box != None:
        x1, y1, x2, y2 = box

        # draw rectangle with opencv and given coordinates
        # .rectangle(frame to draw on, top left corner, bottom right corner, color of box, thickness of outline)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 5)


    cv2.imshow('Image', frame)

    # Termination of webcam 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

