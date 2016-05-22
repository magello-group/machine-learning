from Centroid import Centroid
from Point import Point

def classify(x, y, centroids):
	""" Returns lables """
	lables = []
	for j in xrange(0, len(x)):
		closestDistance = centroids[0].point.distanceSquared(Point(x[j], y[j]))
		lable = centroids[0].lable

		for i in xrange(1, len(centroids)):
			distance = centroids[i].point.distanceSquared(Point(x[j], y[j]))
			if distance < closestDistance:
				closestDistance = distance
				lable = centroids[i].lable

		lables.append(lable)
	return lables


def reCalculateCentroids(x, y, lables, centroids):
	
	newX = [0]  * len(centroids)
	newY = [0] * len(centroids)
	numberOfPoints = [0] *  len(centroids)
	newCentroids = []

	for index in xrange(0, len(x)):
		newX[lables[index]] += x[index]
		newY[lables[index]] += y[index]
		numberOfPoints[lables[index]] += 1	
		
	for index in xrange(0, len(centroids)):
		oldCentroid = centroids[index]

		if numberOfPoints[index] == 0:
			newCentroid = Centroid(oldCentroid.point, oldCentroid.color, oldCentroid.lable)
			newCentroids.append(newCentroid)
			continue

		newX[index] = newX[index] / numberOfPoints[index]
		newY[index] = newY[index] / numberOfPoints[index]
		averageX = (oldCentroid.point.X + newX[index]) / 2
		averageY = (oldCentroid.point.Y + newY[index]) / 2
		newCentroid = Centroid(Point(averageX, averageY), oldCentroid.color, oldCentroid.lable)
		newCentroids.append(newCentroid)

	return newCentroids
