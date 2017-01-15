# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
# add input argument
ap.add_argument("-i","--image",required=True,help="Path to the image")
# add output argument
#ap.add_argument("-o","--output",required=False,help="Path to the output image a$
args = vars(ap.parse_args())

# load the image, grab its dimensions, and show them
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original",image)

# images are just NumPy arrays. The top-left pixel can be found at (0,0)
(b, g, r) = image[225,111]
print "Pixel at (111,225) - Red: {r}, Green: {g}, Blue: {b}".format(r=r,g=g,b=b)

# let's change the value of the pixel at (0, 0) and make it red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0,0]
print "Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r,g=g,b=b)

# Let's access a larger rectangular portion of the image

# compute the center of the image - width and height divided by 2
(cX, cY) = (w/2, h/2)

# since we are using NumPy arrays, we can apply slicing and grab large chunks
# of the image -- let's grab the top-left corner of the image
tl =  image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)

# top-right
tr = image[0:cY, cX:w]
cv2.imshow("Top-Right corner",tr)

# bottom-right
br = image[cY:h,cX:w]
cv2.imshow("Bottom-Right Corner",br)

#  bottom-left
bl = image[cY:h,0:cX]
cv2.imshow("Bottom-Left Corner",bl)

# making the top-left section all green
image[0:cY, 0:cX] = (0,255,0)

# Show the updated image
cv2.imshow("Udated",image)
cv2.waitKey(0)



