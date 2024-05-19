# main function runs everything together for program
import numpy as np
import cv2
from PIL import Image

# webcam function from open cv, creates cam object which can then be used to feed frames
cam = cv2.VideoCapture(0)

# infinite loop to get continious feed of frames
while True:
    # read() returns boolean value stored in cap that says whether frames are being captured or not
    # returns the actual frame and stores in frame
    cap, frame = cam.read()

    # .imshow(name of window, frame object to be shown)
    cv2.imshow('Webcam', frame)



    
    # Termination of webcam 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

