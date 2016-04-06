import numpy as np
import cv2

img = cv2.imread('img-640x640.jpg')

Z = img.reshape((-1, 3))

Z = np.float32(Z)

ret, label, center = cv2.kmeans(
  data=Z,
  K=3,
  bestLabels=None,
  criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0), 
  attempts=10, 
  flags=cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)

print "LABEL:"
print label
print "CENTER:"
print center
res = center[label.flatten()]
print "RES:"
print res

print img.shape
res2 = res.reshape((img.shape))

cv2.imwrite("kmean.jpg", res2);
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
