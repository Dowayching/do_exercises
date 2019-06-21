# USAGE
# python flipping.py --image florida_trip.png

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])

# flip the image horizontally & print specified pointer RGB
flipped = cv2.flip(image, 1)
(b, g, r) = flipped[235, 259]
print("flipe horizontal, (259, 235) = RGB ({}, {}, {})".format (r, g, b))

# flip the image horizontal, 45 degrees rotation, vertical flip &
# print specified pointer RGB
(h, w) = image.shape[:2]
h_flipped = cv2.flip(image, 1)
M = cv2.getRotationMatrix2D((w/2, h/2), 45, 1.0)
rotated = cv2.warpAffine(h_flipped, M, (w, h))
v_flipped = cv2.flip(rotated, 0)
(b, g, r) = v_flipped[189, 441]
print("Horizontal flip -> 45 degree rotate -> veritical flip, (441, 189) =" +
       " RGB ({}, {}, {})".format (r, g, b))
cv2.imshow("1 flip", h_flipped)
cv2.imshow("rotated", rotated)
cv2.imshow("flip", v_flipped)
cv2.waitKey(0)
