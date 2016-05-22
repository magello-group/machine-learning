import matplotlib.pyplot as plt

class Plotter(object):
	"""Plotter just to make plotting easy."""
	def __init__(self, xAxis, yAxis):
		self.xAxis = xAxis
		self.yAxis = yAxis
		plt.ion() # set plot to animated

	def show(self):
		plt.show(block=False)

	def setAxes(self):
		axes = plt.gca()
		axes.set_xlim(self.xAxis)
		axes.set_ylim(self.yAxis)
		
	def plotUnlabledData(self, x, y):
		self.setAxes()
		plt.plot(x, y, 'x', color='black')

	def clear(self):
		plt.clf()

	def plotCentroids(self, centroids):
		self.setAxes()
		for centroid in centroids:
			plt.plot(centroid.point.X, centroid.point.Y, 's', color=centroid.color)
		plt.draw()

	def plotLabledData(self, x, y, labels, centroids):
		self.setAxes()
		for i in xrange(0, len(x)):
			plt.plot(x[i], y[i], 'x', color=centroids[labels[i]].color)
		plt.draw()
