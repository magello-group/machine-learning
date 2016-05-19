# Support vector machine

Support vector machines is a just fancy name for sepetaring points in some general dimension with a plane.

Depending on the type of your kernel that plane can take many shapes.

The one initially used in this lab is a linjear plane.

The lab is broken in some ways. And part of the lab is working through and fixing it and improving the classifier.

Initially we are using 'bad.txt' and 'good.txt' as data sources but later one we will use bigger files that have more data and it will make it easier for our classifier to do a good job.

If you have followed the previous instructions and have everything set-up for the lab you can run the program with:

`python spamFilterLab.py

It will throws an errors but we will solve that soon.

## Instructions

### Make the program compile

In the file 'spamFilterLab.py' there are a couple of TODO:s

One of the todos is breaking the code and are preveting you from running the program.

This needs to be fixed to have a working solution at all.

For each of the data that we get when we read the file we need to label it to either 0 or 1 depending if it is good or bad.

Thus the array found on row 49 should a an array of 0 and 1 that represent the examples array. 0 at every position we have a bad example and 1 for every position we have a good example.

### Remove the random function

There is a random function that shuffles the list. Why is it there? What would happen if you remove it?

### Play with the features

There are some features that are calculated but not put in the features vector that you might want to add!

Not only that but there are some other features that might be good to have. Try and think and figure out what characters a spam might have and try to calculate those features based on the information.

Something that you also need to do is to check the features vector! There is some error in it that is related to rounding that makes one whole feature to be the same no matter what. Better check what is going on and how to fix it.


### Change the different input values for the svm algorithm

So far you should have been using the input files 'good.txt' and 'bad.txt'. Try changing the input files to the larger files called 'badCritiques.txt' and 'goodCritiques.txt' and see what happens.
