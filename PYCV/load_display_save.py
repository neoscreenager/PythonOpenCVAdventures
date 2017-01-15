# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
# add input argument
ap.add_argument("-i","--image",required=True,help="Path to the image")
# add output argument
ap.add_argument("-o","--output",required=False,help="Path to the output image along with complete image name with extension")
args = vars(ap.parse_args())

# load the image and show some basic iformation on it
image = cv2.imread(args["image"])
print "width: %d pixels" % (image.shape[1])
print "height: %d pixels" % (image.shape[0])
print "channels: %d" % (image.shape[2])

# show the image and wait for a keypress
cv2.imshow("Image" , image)
cv2.waitKey(0)

# save the image -- OpenCV handles converting filetypes
# automatically
# If user provide the --ouput argument, only then the file will be saved
# else not
if(args["output"]):
	cv2.imwrite(args["output"],image)

 
