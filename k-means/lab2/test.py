import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random 
from Point import Point

def loadData(fileName):
	"""
    Returns two data sets.
    First return value is the x values and the second one is the y values.
    """
	data = np.loadtxt(fileName)
	dataArray = []
	for i in xrange(0, len(data[0])):
		dataArray.append((data[0][i], data[1][i]))
	random.shuffle(dataArray)
	return dataArray


if __name__ == '__main__':
	plt.ion() # set plot to animated

	var = loadData('trainingData.txt')
	print var
