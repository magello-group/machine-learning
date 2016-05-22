
K-Means clustering
------------------

# Introduction

K-means is an unsupervised clustering algorithm which is used to group a number of points into
K groups (or "clusters"). The process is iterative, starting at (usually) random points and then
iteratively improving the center of each cluster, called the "centriod", until the centroid 
stabilizes. K-means gives best result when the data points are separated in distinct clusters.
K-means main weakness is that the number of clusters must be known beforehand.

This demonstration will help to visualize how the K-Means clustering algorithm works:
http://stanford.edu/class/ee103/visualizations/kmeans/kmeans.html

# Excercise

In this lab we will use the K-Means algorithm to reduce the colors in an image. The alorithm will
take the image (data) as well as the number of colors you want to use in the resulting image (K)
and will then be group the image pixels into K groups, returningthe calculated centroids 
(i.e. the colors to use) and a list of lists containing which cluster each pixel belongs to.

Use the code in kmeans.py as a starting base. Locate the TODO comments and follow the instructions
to create the needed code.

A new image will be generated using OpenCV and displayed on the screen. Close the image by
pressing the any key while having the image in focus!

One possible solution exists in kmeans-solution.py. Please don't peek unless you get stuck! :)

## Apart from python we we use two external libraries:

### Numpy

The central feature of Numpy is the array object class. Arrays are similar to lists in Python,
except that every element of an array must be of the same type, typically a numeric type like
float or int. Arrays make operations with large amounts of numeric data very fast and are
generally much more efficient than lists.

You will use numpy to transform the image bitmap into an array which python can work with.
After you have run your ML algorithm numpy will transform the array back to an image bitmap
which can be displayed.

For more information, read:
http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf

### OpenCV

OpenCV is an Open Source Computer Vision library which contains implementations of several
Machine Learning algorithms, as well as functionality to display and manipulate images.

You can find documentation here:
http://docs.opencv.org/2.4/

In this lab we will use the k-means algorithm of OpenCV. You can find it documented here:
http://docs.opencv.org/2.4/modules/core/doc/clustering.html
