import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Reading and Showing Images

img = cv.imread("Photos/cat_large.jpg")
cv.imshow("Cat", img)
# cv.waitKey(0)

# Reading videos
# capture = cv.VideoCapture("Videos/dog.mp4")
#
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# Resizing and Rescale images/videos
def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
