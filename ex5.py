# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 09:32:36 2022

@author: 52551
"""

import cv2
import numpy as np
 
img = cv2.imread('sangre.png')
 
height, width, c = img.shape
 
i = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('lasang.avi', fourcc, 60, (1575,1024))
 
while True:
    i += 1
     
    # divided the image into left and right part
    # like list concatenation we concatenated
    # right and left together
    l = img[:, :(i % width)]
    r = img[:, (i % width):]
 
    img1 = np.hstack((r, l))
     
    # this function will concatenate
    # the two matrices
    cv2.imshow('animation', img1)
    out.write(img1)
 
    if cv2.waitKey(1) == ord('q'):
       
        # press q to terminate the loop
        cv2.destroyAllWindows()
        break