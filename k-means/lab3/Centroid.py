from Point import Point

class Centroid(object):
	""" Centroid object, has a point and a color and a lable """
	def __init__(self, point, color, lable):
		super(Centroid, self).__init__()
		self.point = point
		self.color = color
		self.lable = lable