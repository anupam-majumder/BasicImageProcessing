import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of color in HSV
    lower_color_range = np.array([110,50,50]) #blue
    upper_color_range = np.array([130,255,255])

    # Threshold the HSV image to get only the selected colors
    mask = cv2.inRange(hsv, lower_color_range, upper_color_range)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('Result',res)
    k = cv2.waitKey(5) & 0xFF
    # Press Esc to exit
    if k == 27:
        break

cv2.destroyAllWindows()

