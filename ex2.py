# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:07:47 2022

@author: Hector Morales 
"""

# importing the module
import cv2

# reading the video
source = cv2.VideoCapture(r"C:\Users\52551\Desktop\Biomed3\DATA\STGEORGES.avi")

source.set(cv2.CAP_PROP_FPS, 4) 


# running the loop
while True:
    # extracting the frames
    ret, img = source.read()
	# converting to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(gray,'4 FPS',(0,50),font,0.8,(0,255,255),3)
	# displaying the video
    cv2.imshow("Live", gray)
	# exiting the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
	
# closing the window
cv2.destroyAllWindows()
source.release()
