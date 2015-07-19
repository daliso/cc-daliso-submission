# example of program that calculates the median number of unique words per tweet.

import sys
import pandas as pd

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')

# after reading each tweet, the number of unique words is appended to this list
uniqueWords = []

for line in inputFile:
    uniqueWords+= [len(set(line.split()))]
    outputFile.write(str(pd.DataFrame(data=uniqueWords).median().values[0])+'\n')
    
               
inputFile.close()
outputFile.close()