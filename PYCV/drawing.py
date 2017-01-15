# import the necessary packages
import numpy as np
import cv2

# initialize our canvas as a 300x300 with 3 channels RGB, with black background
canvas = np.zeros((300,300,3),dtype="uint8")

# draw a green line from the top-left corner of our canvas to the
# bottom-right
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
 
# now, draw a 3 pixel thick red line from the top-right corner to the
# bottom-left
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
 
# draw another rectangle, this time we'll make it red and 5 pixels thick
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
 
# let's draw one last rectangle: blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# reset our canvas and draw a white circle at the center of the canvas with
# increasing radii - from 25 pixels to 150 pixels
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2)
white = (255, 255, 255)
count = 2
for r in xrange(0, 175, 25):
	white = (0+r,180,255-r)
	if(count%2==0):
		cv2.circle(canvas, (centerX, centerY), r, white,-1)
	else:
		cv2.circle(canvas, (centerX, centerY), r, white)
	count=count+1
	cv2.waitKey(0)
	cv2.imshow("Canvas", canvas)
 
# show our work of art
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# let's go more crazy and draw 25 random circles
for i in xrange(0, 25):
	# randomly generate a radius size between 5 and 200, generate a random
	# color, and then pick a random point on our canvas where the circle
	# will be drawn
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size = (3,)).tolist()
	pt = np.random.randint(0, high=300, size = (2,))
 
	# draw our random circle
	cv2.circle(canvas, tuple(pt), radius, color, -1)
 
# Show our masterpiece
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
