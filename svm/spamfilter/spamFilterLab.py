from Reader import Reader
from FeaturesUtilityFunctions import wordCounter, countUniqueChars, countNumberOfChars, countUniqueWords, checkForRepetition
import random 
import numpy as np


def getFeature(critique, label):
	" construct feature vector" 
	feature = []
	# Calculate a number of features and put them into an array.
	# What features are relevant?
	# Are there any missing features?
	chars = countNumberOfChars(critique)
	uniqueChars = countUniqueChars(critique)
	weightedUniqueChars = uniqueChars/chars

	feature.append(chars)
	feature.append(uniqueChars)
	feature.append(weightedUniqueChars)

	# Calculate some features based on the words 
	counterForWords = wordCounter(critique)
	uniqueWords = countUniqueWords(counterForWords)
	hasRepetition = checkForRepetition(counterForWords)

	feature.append(uniqueWords)
	feature.append(hasRepetition)

	# Finally add the label
	feature.append(label)

	return feature

def make_np_array_XY(xy):
	print "make_np_array_XY()"
	a = np.array(xy)
	x = a[:,0:-1]
	print x
	y = a[:,-1]
	print y
	return x,y


if __name__ == '__main__':
	reader = Reader()
	# Read the data from out example files
	badExamples = reader.read('bad.txt', '|')
	goodExamples = reader.read('good.txt', '|')

	# Aggregate the data into one array
	critiques = badExamples + goodExamples

	# Label the data 0 for bad 1 for good
	# 'labels' should be an array with the same lenth as 'critiques' 
	# populated with 0, one for each entry in 'badExamples'
	# and 1 one for each entry in  'goodExamples' with 1. 
	labels = [0]*len(badExamples) + [1]*len(goodExamples)

	# Lets create the features we will use for analysis.
	featureVector = []
	for i in range(len(critiques)):
		feature = getFeature(critiques[i], labels[i])
		featureVector.append(feature)


	# Lets create two sets of data! One for training and
	# one for testing to see how good our algorithm was.
	# But first shuffle the list so taht every run will be unique
	random.shuffle(featureVector)
	cut = int(len(featureVector)/2) # Split in half, maybe test to change this limit!
	trainData = featureVector[:cut]
	testData = featureVector[cut:]

	make_np_array_XY(trainData)










