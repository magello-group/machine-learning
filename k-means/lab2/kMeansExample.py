import numpy as np
import matplotlib.cm as cm
import KMeans as kmeans

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


if __name__ == '__main__':

	# Init the plotter with some axis parameters
	plotter = Plotter([-20, 80], [-20, 80])

	#Load data
	trainingX, trainingY = loadData('trainingData.txt')

	print "Init - show the data..."
	plotter.plotUnlabledData(trainingX, trainingY)
	plotter.show()
	raw_input('Press enter to continue')

	# Define the centroids based on some points
	print "Init - Create the first cluster points and plot them..."
	clusterPoints = [Point(2, 3), Point(35, 20), Point(40, 40), Point(60, 60), Point(30, 30)]
	centroids = getCentroids(clusterPoints)
	plotter.plotCentroids(centroids)
	print "Init complete..."
	raw_input('Press enter to continue and to start the algorithm.')

	# Run the algorith 10 times
	for x in xrange(1,10):
		# Get lables
		labels = kmeans.classify(trainingX, trainingY, centroids)
		# Plot the labled data
		print "Plot the labled data."
		plotter.clear()
		plotter.plotCentroids(centroids)
		plotter.plotLabledData(trainingX, trainingY, labels, centroids)
		raw_input('Press enter to continue')

		# Recalculated the centroids and unlable the data so to say...
		print "Plot the new centroids."
		plotter.clear()
		plotter.plotUnlabledData(trainingX, trainingY)
		centroids = kmeans.reCalculateCentroids(trainingX, trainingY, labels, centroids)
		plotter.plotCentroids(centroids)
		raw_input('Press enter to continue')



	raw_input("Trying out the clusters with some new data... press enter to continue")

	rawDataX, rawDataY = loadData('largeDataSet.txt')
	labels = kmeans.classify(rawDataX, rawDataY, centroids)
	plotter.clear()
	plotter.plotCentroids(centroids)
	plotter.plotLabledData(rawDataX, rawDataY, labels, centroids)
	
	raw_input('Finished. Press enter to close.')








