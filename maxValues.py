# imports:
import numpy as np
import cv2

# image path
path = "D://opencvImages//"
fileName = "testMat2.png"

# Reading an image in default mode:
inputImage = cv2.imread(path + fileName)

# Get max value and print it:
maxValue = inputImage.max()
print("Max BGR value is: "+str(maxValue))

# Display the image:
cv2.imshow("inputImage [BGR]", inputImage)
cv2.waitKey(0)

# Convert BGR to grayscale:
grayImg = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

# Get max value and print it:
maxValue = grayImg.max()
print("Max Gray value is: "+str(maxValue))

# Display the image:
cv2.imshow("inputImage [grayImg]", grayImg)
cv2.waitKey(0)