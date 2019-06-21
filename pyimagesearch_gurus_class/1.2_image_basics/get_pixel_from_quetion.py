# USAGE
# python getting_and_setting.py --image florida_trip.png

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-x", "--x_axis", required=True, help="X-axis")
ap.add_argument("-y", "--y_axis", required=True, help="Y-axis")
args = vars(ap.parse_args())

# load the image, grab its dimensions, and show it
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# print the RGB for specified pointer
y = int(args["x_axis"])
x = int(args["y_axis"])
(b, g, r) = image[x, y]
print("Pixel at ({x}, {y}) - Red: {r}, Green: {g}, Blue: {b}".format(
    x=x, y=y, r=r, g=g, b=b))

