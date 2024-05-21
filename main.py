# main function runs everything together for program
import numpy as np
import cv2
from PIL import Image
import mask

# webcam function from open cv, creates cam object which can then be used to feed frames
cam = cv2.VideoCapture(0)

# infinite loop to get continious feed of frames
while True:
    # read() returns boolean value stored in cap that says whether frames are being captured or not
    # returns the actual frame and stores in frame
    cap, frame = cam.read()

    # convert image to hsv
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # for dilation
    """
    kernel = np.ones((5, 5), np.uint8)
    mask3 = cv2.dilate(total_mask, kernel)
    """
    

    cv2.imshow('Image', mask.bounding_box(frame, hsv_frame))

    # Termination of webcam 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

