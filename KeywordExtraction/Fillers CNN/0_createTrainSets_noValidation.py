# STUFF TO INSTALL:
# pip install tensorflow==1.14
# pip install keras==2.2.5

import csv
import os
import math
import random

dictionary={}

# Encoding utf-8-sig makes sure that non-alphabetical characters don't get appended to the first entry
csvfile=open(os.getcwd()+"/Sentences_Vids123456_longerFillerDataset.csv", encoding="utf-8-sig",mode="r")
reader = csv.reader(csvfile)

highestWordCount=0

# Make a dictionary where the keys are the category numbers (1-16) and the values are an array of all the sentences/phrases falling into each category
for row in reader:
    # print(row[0])

    if len(row[0].split())>highestWordCount:
        highestWordCount=len(row[0].split())

    if row[1] in dictionary:
        dictionary[row[1]].append(row[0])
    else:
        dictionary[row[1]]=[row[0]]

print(dictionary)
# print(highestWordCount)

# Make train (80%), validation (20%)
fullTrainList=[]

for key, value in dictionary.items():
    shuffledList = random.sample(value, len(value))
    print(len(shuffledList))

    if key=="2":
        print("Hello")
        shuffledList=shuffledList[:int(math.floor(float(len(shuffledList))*0.30))]
        print(len(shuffledList))

    trainSet=shuffledList

    for x in trainSet:
        fullTrainList.append([x, key])

# Write the train, validation, and test sets to CSVs
def writecsv(filename, array):
    # opening the csv file in 'w+' mode
    file = open(filename+'.csv', 'w+', newline='')

    # writing the data into the file
    with file:
        write = csv.writer(file)
        write.writerows(array)

writecsv("0_trainSet",fullTrainList)