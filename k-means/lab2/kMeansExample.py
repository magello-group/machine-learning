import numpy as np
import matplotlib.cm as cm
from Point import Point
from Plotter import Plotter
from Centroid import Centroid

def loadData(fileName):
	"""
    Returns two data sets.
    First return value is the x values and the second one is the y values.
    """
	data = np.loadtxt(fileName)
	return (data[0], data[1])
	

def getCentroids(clusterPoints):
	centroids = []
	colors = iter(cm.rainbow(np.linspace(0, 1, len(clusterPoints))))
	for index in xrange(0, len(clusterPoints)):
		centroids.append(Centroid(clusterPoints[index], next(colors), index))
	return centroids

def classify(x, y, centroids):
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

def calculateNewCentroids(x, y, lables, centroids):
	#for centroid in centroids:
	newX = [0]  * len(centroids)
	newY = [0] * len(centroids)
	numberOfPoints = [0] *  len(centroids)

	for index in xrange(0, len(x)):
		newX[lables[index]] += x[index]
		newY[lables[index]] += y[index]
		numberOfPoints[lables[index]] += 1	
		
	for index in xrange(0, len(centroids)):
		newX[index] = newX[index] / numberOfPoints[index]
		newY[index] = newY[index] / numberOfPoints[index]
		centroids[index].point.X = newX[index]
		centroids[index].point.Y = newY[index]


if __name__ == '__main__':

	# Init the plotter with some axis parameters
	plotter = Plotter([-20, 80], [-20, 80])

	#Load data
	trainingX, trainingY = loadData('trainingData.txt')

	print "Init..."
	plotter.plotUnlabledData(trainingX, trainingY)
	plotter.show()
	raw_input('Press enter to continue')

	# Define the centroids based on some points
	clusterPoints = [Point(2, 3), Point(35, 20), Point(40, 40)]
	centroids = getCentroids(clusterPoints)
	plotter.plotCentroids(centroids)
	print "Init complete..."
	raw_input('Press enter to continue')

	# Run the algorith 10 times
	for x in xrange(1,10):
		# Get lables
		labels = classify(trainingX, trainingY, centroids)
		# Plot the labled data
		plotter.clear()
		plotter.plotCentroids(centroids)
		plotter.plotLabledData(trainingX, trainingY, labels, centroids)
		raw_input('Press enter to continue')

		# Recalculated the centroids and unlable the data so to say...
		plotter.clear()
		plotter.plotUnlabledData(trainingX, trainingY)
		calculateNewCentroids(trainingX, trainingY, labels, centroids)
		plotter.plotCentroids(centroids)
		a = raw_input('Press enter to continue')

	








