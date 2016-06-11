# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

import numpy as np
# install python-opencv package 
# sudo apt-get install python-opencv (linux)
import cv2

# enter the name of the video file you want to play
cap = cv2.VideoCapture('output.avi')

while(cap.isOpened()):
    	ret, frame = cap.read()
	if ret==True:
	    	cv2.imshow('frame',frame)

		# cv2.waitKey():
		# if the number is too high video will be slow
		# if the number is too low video will be fast
		key = cv2.waitKey(40)
		# press ESC key to exit
		if key == 27:
			break
	else:
		break

# release everything if job is finished
cap.release()
cv2.destroyAllWindows()
