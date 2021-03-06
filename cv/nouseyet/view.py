import numpy as np
import cv2
import time as t
import sys

cap = cv2.VideoCapture(0)
mark = 0
while(True):
    ret, frame = cap.read()
    cv2.namedWindow("calib")
    #cv2.imshow('frame',cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    #cv2.imshow('frame', cv2.cvtColor(frame, cv2.COLOR_BGR2HSV))
    hsv_frame = cv2.GaussianBlur(frame, (13,13), 0, 0)
    #hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv_frame)

    print ((str)(t.time()))[-4:]
    # waitkey is a must-do operation, else there will be no images showed
    if cv2.waitKey(1) & 0xFF == ord('o'):
        if len(sys.argv) < 2: 
            name = (str)(t.time())
            cv2.imwrite(name + '.png', frame)
            print (str)(name + '.png ' + 'saved')
        else:
            cv2.imwrite(sys.argv[1]+'.png', frame)
            print sys.argv[1]+'.png ' + "saved"
    mark = mark + 1
    #cv2.imwrite("haha/"+(str)(mark)+'.png', frame)
    cv2.waitKey(1)
 
#whi#le(True):
#    # Capture frame-by-frame
#    ret, frame = cap.read()
#
#    # Our operations on the frame come here
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#    # Display the resulting frame
#    cv2.imshow('frame',frame)
#
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#
## When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
