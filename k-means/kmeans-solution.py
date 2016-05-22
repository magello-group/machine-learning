import numpy
import cv2

# Read the image which should be processed. It will be stored in memory as
# an array of arrays of arrays. In the case of an image of size 32x32 it will contain
# 32 columns -> 32 Rows -> Pixel [R,B,G]
# Thre images are available, you can raplce them with your own if you want
#  img-640x640.jpg - Image of a cat
#  img-32x32.jpg   - Small image used for debugging
#  red.jpg         - Small single color image, used for debugging
img = cv2.imread('img-640x640.jpg')

# TODO
# Reshape the image into an array of arrays, each row containing the
# value of one pixel split inte Red, Green and Blue color. In the case 
# of an image of size 32x32 it must contain 1024 Rows -> Pixel [R,B,G]
# http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.reshape.html
Z = img.reshape((-1, 3))

# TODO
# Use numpy to transform the binary image to an array of arrays of float32,
# each array containing the Red, Blue and Green representation of the image.
# http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.ndarray.astype.html
Z = numpy.float32(Z)

# TODO
# Run the cv2.kmeans algorithm, where K should be the number of colors
# you want in the processed image
# http://docs.opencv.org/2.4/modules/core/doc/clustering.html
ret, label, center = cv2.kmeans(
  # Input data
  data=Z,
  # Number of iterations
  K=?4,
  bestLabels=None,
  # Algorithm termination criteria. when to stop iterating (because centroids
  # are not moving anymore) and maximum iterations
  # see documentation for more information
  criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0), 
  # Number of attempts using different initial labelings.
  attempts=10,
  # How to select initial centers
  flags=cv2.KMEANS_PP_CENTERS)

# Set to 1 to enable printing of debug information
if 0:
  numpy.set_printoptions(edgeitems=32) #Enable debug printing of larger part of numpy array
  print "Reshaped Input Data"
  print Z
  print "K-Means calculated labels"
  print label
  print "K-Means calculated colors"
  print center

# TODO
# Use numpy to convert the float32 array to an uint8 array
# http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.ndarray.astype.html
center = numpy.uint8(center)

# Map the calculated colors using the the labels into a new image
res = center[label.flatten()]

# TODO
# Restore the original image dimensions
# http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.reshape.html
res = res.reshape(img.shape)

# This code will display the result. Close the image by clicking in the image and
# pressing the any key
cv2.imwrite("kmean.jpg", res);
cv2.imshow('res2',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
