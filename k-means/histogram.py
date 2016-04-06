import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img-640x640.jpg')
Z = img.reshape((-1, 1))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
ret, label, center = cv2.kmeans(
  data=Z,
  K=2,
  bestLabels=None,
  criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0), 
  attempts=10, 
  flags=cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

x = np.random.randint(25,100,25)
y = np.random.randint(175,255,25)
z = np.hstack((x,y))
z = z.reshape((50,1))
z = np.float32(z)
plt.hist(z,256,[0,256]),plt.show()

#cv2.imwrite("kmean.jpg", res2);
#cv2.imshow('res2',res2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
