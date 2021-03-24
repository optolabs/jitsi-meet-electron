# test_image.py

import cv2
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

# frame = cv2.imread('677f69c802855af82846a79cfef2a3a8.png')
frame = cv2.imread('test.jpg')
cv2.imshow('Greasy Adult Film Actor',frame)

print(frame)

retval, jpg_frame = cv2.imencode('.jpg', frame)

# print(jpg_frame)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()