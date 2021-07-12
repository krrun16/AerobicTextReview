# Github repository where I got the Deepsegment library from: https://github.com/notAI-tech/deepsegment
# (takes long paragraph without periods and turns it into sentences)
# pip install --upgrade deepsegment

from deepsegment import DeepSegment
import os
import csv

# function to return array of lines from a text file
def getTextLines(txtFilename) -> [str]:
    workoutTextFile = open(txtFilename, "r")

    lineTextArray=[]

    for lineText in workoutTextFile:
        # Get rid of the \n
        lineTextArray.append(lineText.rstrip('\n').lower())

    return lineTextArray

# function to return array of each word from a text file
def getTextWords(txtFilename) -> [str]:
    workoutTextFile = open(txtFilename, "r")
    wordsArray=[]

    for lineText in workoutTextFile:
        for word in lineText.rstrip('\n').lower().split():
            wordsArray.append(word)

    return wordsArray

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

transcriptFiles=["Video_1_Hasfit.txt",
                 "Video_2_nikeTrainerClub.txt",
                 "Video_3_BodyProject.txt",
                 "Video_4_MadFit.txt",
                 "Video_5_ChloeTing.txt",
                 "Video_6_BeFit.txt"]

# The default language is 'en' for English
segmenter = DeepSegment('en')

mySentencesData=[]

for transcriptFilename in transcriptFiles:
    txtFilename = os.path.split(os.path.abspath(os.getcwd()))[0] + "/Video Analysis/Transcripts/"+transcriptFilename
    textLines = getTextLines(txtFilename=txtFilename)
    textWords = getTextWords(txtFilename=txtFilename)
    fullText = getFullText(txtFilename=txtFilename)

    thisVideoSentencesArray = segmenter.segment_long(fullText)

    for sentence in thisVideoSentencesArray:
        mySentencesData.append([sentence, transcriptFilename])

# function to write an array to csv
def makeKeywordCSV(mySentencesData,csvFilename):
    with open(csvFilename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for mySentence in mySentencesData:
            writer.writerow([mySentence[0], mySentence[1]])

makeKeywordCSV(mySentencesData,os.getcwd()+"/Sentences_Vids2.csv")