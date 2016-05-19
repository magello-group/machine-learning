import collections
import numpy as np

def wordCounter(s):
	cnt = collections.Counter()
	words = s.split()

	for w in words:
		cnt[w] += 1

	return cnt

def countUniqueChars(s):
	s2 = ''.join(set(s))
	return len(s2)

def countNumberOfChars(s):
	return len(s)



def totalWords(cnt):
    sum = 0
    for k in dict(cnt).keys():
        sum += int(cnt[k])

    return sum

def countUniqueWords(cnt):
	sum = 0
	for k in dict(cnt).keys():
		sum += int(cnt[k])
	return sum

def checkForRepetition(cnt):
	for k,v in cnt.most_common(1):
		freq = v/totalWords(cnt)
		if freq > 0.5:
			return 1
	return 0



def extractDataAsNumPyArray(data):
	a = np.array(data)
	x = a[:,0:-1]
	return x

def extractLabelAsNumPyArray(data):
	a = np.array(data)
	y = a[:,-1]
	return y


