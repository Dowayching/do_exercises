# USAGE
# python rotate.py --image grand_canyon.png

# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])

# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

# rotate our image by -30 degrees
M = cv2.getRotationMatrix2D((cX, cY), -30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
(b, g, r) = rotated[254, 335]
print("Rotate -30 degrees: (335, 254) = RGB ({}, {}, {})".format (r, g, b))

# rotate our image by 110 degrees
M = cv2.getRotationMatrix2D((cX, cY), 110, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
(b, g, r) = rotated[136, 312]
print("Rotate 110 degrees: (312, 136) = RGB ({}, {}, {})".format (r, g, b))

# rotate our image by 88 degrees about coordinate is (50, 50)
M = cv2.getRotationMatrix2D((50, 50), 88, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
(b, g, r) = rotated[10, 10]
print("Rotate 88 degrees: (10, 10) = RGB ({}, {}, {})".format (r, g, b))


