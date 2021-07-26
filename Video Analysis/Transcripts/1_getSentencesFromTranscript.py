from deepsegment import DeepSegment
import os

segmenter = DeepSegment('en')
mySentences=[]

transcriptFiles=["Video_9_HIIT.txt"]

from os.path import dirname as up

# function to return full text from a file
def getFullText(txtFilename) -> str:
    # Read in a text file one line at a time
    workoutTextFile = open(txtFilename, "r")
    fullText = ""

    for lineText in workoutTextFile:
        # Get rid of the \n
        fullText += lineText.rstrip('\n')+" "

    fullText = fullText.lower()
    return fullText

for transcriptFilename in transcriptFiles:
    txtFilename = os.getcwd() + "/" + transcriptFilename
    fullText = getFullText(txtFilename=txtFilename)

    fullText = fullText.lower()

    thisVideoSentencesArray = segmenter.segment_long(fullText)

    for sentence in thisVideoSentencesArray:
        mySentences.append([sentence, transcriptFilename])

import csv
import os

with open(os.getcwd()+"/Fillers_Video_9_HIIT.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    for mySentence in mySentences:
        writer.writerow([mySentence[0], mySentence[1]])