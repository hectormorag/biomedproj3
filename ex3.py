# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:58:53 2022

@author: Hector Morales
"""

import cv2
import os
import re

image_folder = r"C:\Users\52551\Desktop\Biomed3\pieton"
video_name = 'pieton.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".bmp")]
images = sorted(images, key=lambda x: int(re.search('\d+', x).group(0)))
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()