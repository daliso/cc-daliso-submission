Insight Data Engineering - Coding Challenge
===========================================================

Please find included the coding challenge submission for Daliso Zuze

This was written in Python 2.7.6

I have used the following two Python libraries for my solution:

import sys
import pandas as pd


Approach to Feature 1 : Words Tweeted
=====================================

My approach was inspired by the work that I have been doing with Apache Spark,
the general approach is MAP > REDUCE

For the MAP part, each word tweeted is mapped to a pair tuple (word, 1)
The REDUCE part groups all the pair tuples by word and sums the values

I made use of Dataframe in pandas to make this easier. It provides similar functionality to pySpark.

This approach is efficient because it avoids the cost of making insertions into a
dictionary, which would become very slow as the dataset becomes larger.



Approach to Feature 2: Median Unique
====================================

For this feature, I make use of Python's conversion of lists to sets to get the 
unique words. 

I append the number of unique tweets to a list one at a time, and on each iteration
make use of pandas Dataframe to calculate the median, and write this to the output file.