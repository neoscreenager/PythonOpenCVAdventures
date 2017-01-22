#import the necessarry packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the argguments
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original",image)

# grab the dimensions of the image and calculate the center of the image
(h,w) = image.shape[:2]
(cX,cY) = (w/2,h/2) # because x is width and y is height of the image

# rotate the image by 45 degrees
M = cv2.getRotationMatrix2D((cX,cY),45,1.0) # center, degree and scale
rotated = cv2.warpAffine(image,M,(w,h) ) # image, rotation matrix and output dimensions
cv2.imshow("Rotated by 45 Degrees",rotated)

# rotate the image by -90 degrees
M = cv2.getRotationMatrix2D((cX,cY),-90,1.0)
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated by -90 Degrees" , rotated)

# rotate our image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((50, 50), 88, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
(b,g,r) = rotated[10,10]
print "R: {r} , G : {g}, B :{b}".format(r=r,g=g,b=b)
cv2.imshow("Rotated by Offset & 45 Degrees", rotated)

# finally, let's use our helper function in imutils to rotate the image by
# 180 degrees (flipping it upside down)
rotated = imutils.rotate(image, 110)
cv2.imshow("Rotated by 180 Degrees", rotated)
(b,g,r) = rotated[136,312]
#print "R : {r} , G : {g}, B :{b}".format(r=r,g=g,b=b)
cv2.waitKey(0)




