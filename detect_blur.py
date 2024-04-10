# import the necessary packages
from imutils import paths
import argparse
import cv2
import numpy as np

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

def sharp_or_blur(image, blur_threshold, threshold):
    print("Blur Threshold: ", blur_threshold)
    if blur_threshold < threshold:
        # Apply sharpening techniques
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened = cv2.filter2D(image, -1, kernel)
        cv2.imwrite('sharpened_image.jpg', sharpened)
        print("Image sharpened and saved as 'sharpened_image.jpg'")
    else:
        # Apply blurring techniques
        blurred = cv2.blur(src=image, ksize=(5, 5))
        cv2.imwrite('blurred_image.jpg', blurred)
        print("Image blurred and saved as 'blurred_image.jpg'")

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

threshold = args["threshold"]

image = cv2.imread(args["images"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_threshold = variance_of_laplacian(gray)
sharp_or_blur(image, blur_threshold, threshold)

