import numpy
import cv2

#Enable debug printing of larger part of numpy array
numpy.set_printoptions(edgeitems=32)

# Read the image which should be processed. It will be stored in memory as
# an array of arrays of arrays. In the case of an image of size 32x32 it will contain
# 32 columns -> 32 Rows -> Pixel [R,B,G]
img = cv2.imread('img-32x32.jpg')

# Reshape the image into an array of arrays, each row containing the
# value of one pixel split inte Red, Green and Blue color. In the case 
# of an image of size 32x32 it must contain 1024 Rows -> Pixel [R,B,G]
Z = img.reshape((-1, 3))

# Use numpy to transform the binary image to an array of arrays of float32,
# each array containing the Red, Blue and Green representation of the image
Z = numpy.float32(Z)

# Run the cv2.kmeans algorithm, where K should be the number of colors
# you want in the processed image
ret, label, center = cv2.kmeans(
  data=Z,
  K=4,
  bestLabels=None,
  criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0), 
  attempts=10, 
  flags=cv2.KMEANS_RANDOM_CENTERS)

print "Reshaped Input Data"
print Z
print "K-Means calculated labels"
print label
print "K-Means calculated colors"
print center

# Use numpy to convert the float32 array to an uint8 array
center = numpy.uint8(center)

# Map the calculated colors using the the labels into a new image
res = center[label.flatten()]

# Restore the original image dimensions
res = res.reshape(img.shape)

# This code will display the result. Close the image by clicking in the image and
# pressing the any key
cv2.imwrite("kmean.jpg", res);
cv2.imshow('res2',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
