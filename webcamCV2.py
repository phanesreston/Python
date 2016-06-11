# works in linux
import numpy as np
# install python-opencv package 
# sudo apt-get install python-opencv (linux)
import cv2

# Define the codec and create VideoWriter object
cap = cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
    	# writes frame
        out.write(frame)
        cv2.imshow('frame',frame)

	# press ESC to exit
	key = cv2.waitKey(20)
        if key == 27:
        	break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
