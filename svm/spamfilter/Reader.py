class Reader:

    def read(self, fileName, delimiter):
    	f = open(fileName, 'r')
    	data = f.read().split(delimiter)
    	f.close()
    	return data

