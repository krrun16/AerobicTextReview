from deepsegment import DeepSegment
import keras
from keras.preprocessing import sequence
import nltk
import os
import csv

def getPercentageSilence(cleanTimestampsFilename):
    cleanTimestampsCSV=open(cleanTimestampsFilename)
    reader = csv.reader(cleanTimestampsCSV)
    allRows=[]

    for row in reader: # each row is a list
        # Data is originally in string format
        if row[1] != "" and row[2] != "":
            allRows.append([row[0],row[1],row[2]])

    print(allRows)
    totalTime=allRows[len(allRows)-1][2]

    totalSilence=0
    for i in range(len(allRows)-1):
        try:
            nextFloatNumber=float(allRows[i+1][1])
            firstFloatNumber=float(allRows[i][2])
            totalSilence += nextFloatNumber-firstFloatNumber
        except:
            totalSilence+=0

    return round((float(totalSilence)/float(totalTime))*100,2)