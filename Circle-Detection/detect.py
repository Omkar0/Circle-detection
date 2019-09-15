# import dependencies
import numpy as np
import argparse
import cv2

# Initialize the list
Pipe_count, x_count, y_count = [], [], []

# Pass image path while executing the command
# for example - python detect.py --image ./images/pipe-webetron.jpeg
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# Or directly pass the path of the image
# image = cv2.imread('./images/pipe-webetron.jpeg')
image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray,(5,5), 0)

# gray = cv2.medianBlur(gray, 5)
# detect circles in the image
# You can manipulate the value within the Houghcircle to get your circle detected

# Type 1
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.6,75)

# Type 2
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.6,12,param1=50,param2=28,minRadius=18,maxRadius=32)

# Type 3
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.2,12,param1=50,param2=28,minRadius=14,maxRadius=28)

# Type 4
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.6,12,param1=50,param2=28,minRadius=18,maxRadius=32)

# Type 5
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2,20,param1=60,param2=20,minRadius=40,maxRadius=40)

if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:

                cv2.circle(output, (x, y), r, (0, 255, 0), 2)
                cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0, 128, 255),-1)
                Pipe_count.append(r)
                x_count.append(x)
                y_count.append(y)
        # show the output image
        cv2.imshow("gray", output)
        # cv2.imshow("output", np.hstack([image, output]))
        cv2.waitKey(0)

print(len(Pipe_count))
print(Pipe_count)  # Total number of radius
print(x_count)     # X co-ordinate of circle
print(y_count)     # Y co-ordinate of circle
