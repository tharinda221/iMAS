import numpy as np
import cv2

# Create a black image
img = np.zeros((100,150,3), np.uint8)

# Write some Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Moving!',(10,50), font, 1,(255,255,255),2)

#Display the image
cv2.imshow("img",img)

cv2.waitKey(0)