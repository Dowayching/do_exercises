# USAGE
# python arithmetic.py --image grand_canyon.png

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])

# add 75 to each image pixels
M = np.ones(image.shape, dtype = "uint8") * 75
added = cv2.add(image, M)
(b, g, r) = added[152, 61]
print("add 75 to all pixels, (61, 152) = RGB ({}, {}, {})".format(r, g, b))

