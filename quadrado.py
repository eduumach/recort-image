import cv2
from PIL import Image
from numpy import asarray


image = Image.open("frame1_000000.PNG")
array = asarray(image)

cv2.rectangle(array, [1002-15, 299-20, 42, 39], (0, 255, 0))
cv2.imshow("Canvas", array)
cv2.waitKey(0)