import cv2
import numpy as np
vid = cv2.VideoCapture(0)
while(1):
  _, image = vid.read()
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  lower_range = np.array([110,50,50])
  upper_range = np.array([130,255,255])
  mask = cv2.inRange(hsv,lower_range,upper_range)
  cv2.imshow('image_window_name',image)
  cv2.imshow('mask_window_namw',mask)
  cv2.waitKey(5) 
cv2.destroyAllWindows()
