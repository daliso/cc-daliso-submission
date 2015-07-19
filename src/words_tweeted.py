# example of program that calculates the total number of times each word has been tweeted.
import sys
import pandas as pd

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')

# This holds tuples of (word,1)
bagOfWords = []

for line in inputFile:
    bagOfWords+=[(word,1) for word in line.split()]
    
# This is where the Reduce by Key is done to create totals for the number of times each word appears
groupedAndSummedWords = pd.DataFrame(data=bagOfWords, columns=['word', 'countOfWord']).groupby('word').sum()

outputFile.write(groupedAndSummedWords.to_string(index_names=False, header=False))
                
inputFile.close()
outputFile.close()