import cv2
import time
from utils import test_name

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
videoWriter = cv2.VideoWriter(test_name + 'video' +'.avi', fourcc, 20.0, (640,480))
print('Capturing Video now ...')

try:
	while (True):
		ret, frame = capture.read()
		 
		if ret:
		    cv2.imshow('video', frame)
		    videoWriter.write(frame)

		if cv2.waitKey(1) == 27:
		    break
	 
	capture.release()
	videoWriter.release()
	 
	cv2.destroyAllWindows()

# Save when the user exits
except KeyboardInterrupt:
    print('Video Closed')
