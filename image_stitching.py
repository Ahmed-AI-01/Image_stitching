import numpy as np
import cv2
import imutils
import glob

image_path = glob.glob("drone1/*.jpg")
images = []


for img in image_path:
    image = cv2.imread(img)
    images.append(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

image_stitch = cv2.Stitcher_create()

error, stitched = image_stitch.stitch(images)


if not error:
    cv2.imwrite("output.jpg", stitched)
    cv2.imshow("Stitched Image", stitched)
    cv2.waitKey(0)