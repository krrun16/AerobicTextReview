import nltk
import urllib.request

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.corpus import wordnet

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

import csv
import os

# NEXT STEPS:
# Need to figure out how to identify similar phrases (not just individual words)
# Implement this for every row in table 1, 2, and 3 of the taxonomy

# Figure out how to actively convert the audio into words/sentences and then run the script
#     after each sentence

# For the poster/paper, we would have to create a test dataset where we annotated
#     the whole script for the different word/phrase types and then see the script's
#     accuracy in identifying all of them?

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
        fullText += lineText.rstrip('\n')

    fullText = fullText.lower()
    return fullText

# function to lemmatize (stem) the original words and then return all possible synonym
def getLemmatizeArray(myWords) -> [str]:
    # Lemmatize (getting the stem of a word and it outputs a real word)
    lemmatizer = WordNetLemmatizer()
    myWordsLemm = []

    for word in myWords:
        myWordsLemm.append(lemmatizer.lemmatize(word, pos="v"))
        myWordsLemm.append(lemmatizer.lemmatize(word, pos="n"))
        myWordsLemm.append(lemmatizer.lemmatize(word, pos="a"))
        myWordsLemm.append(lemmatizer.lemmatize(word, pos="r"))

    # Remove duplicate lemmatize results
    myWordsLemm = list(set(myWordsLemm))
    return myWordsLemm

# function to lemmatize (stem) the original words and then return all possible synonym
def getSynonymArray(myWordsLemm) -> [str]:
    # Get synonym
    myWordsSynonym = []
    for word in myWordsLemm:
        for synonym in wordnet.synsets(word):
            for lemma in synonym.lemmas():
                myWordsSynonym.append(lemma.name().replace("_", " "))

    return myWordsSynonym

# function to count the number of instances of each synonym in the string
def getSynonymDictionary(synonymList,fullText) -> {str:int}:
    mySynonymDictionary = {}
    for synonym in synonymList:
        mySynonymDictionary[synonym] = fullText.count(synonym)

    return mySynonymDictionary

# function to write a dictionary to csv
def makeSynonymCSV(synonymDictionary,csvFilename):
    with open(csvFilename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in synonymDictionary.items():
            writer.writerow([key, value])

txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_Hasfit.txt"
textLines=getTextLines(txtFilename=txtFilename)
textWords=getTextWords(txtFilename=txtFilename)
fullText=getFullText(txtFilename=txtFilename)
synonymArray=getSynonymArray(["squat","jumping jack"])
synonymDictionary=getSynonymDictionary(synonymArray,fullText)
makeSynonymCSV(synonymDictionary,"testingFunctionFamiliarExercisePhrases.csv")

txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_Hasfit.txt"
textLines=getTextLines(txtFilename=txtFilename)
textWords=getTextWords(txtFilename=txtFilename)
fullText=getFullText(txtFilename=txtFilename)
synonymArray=getSynonymArray(["arm","leg", "head"])
synonymDictionary=getSynonymDictionary(synonymArray,fullText)
makeSynonymCSV(synonymDictionary,"testingFunctionBodyParts.csv")

txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_Hasfit.txt"
textLines=getTextLines(txtFilename=txtFilename)
textWords=getTextWords(txtFilename=txtFilename)
fullText=getFullText(txtFilename=txtFilename)
synonymArray=getSynonymArray(["up","left","right","down"])
synonymDictionary=getSynonymDictionary(synonymArray,fullText)
makeSynonymCSV(synonymDictionary,"testingFunctionDirectionToMove.csv")

txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_Hasfit.txt"
textLines=getTextLines(txtFilename=txtFilename)
textWords=getTextWords(txtFilename=txtFilename)
fullText=getFullText(txtFilename=txtFilename)
synonymArray=getSynonymArray(["feel","stretch"])
synonymDictionary=getSynonymDictionary(synonymArray,fullText)
makeSynonymCSV(synonymDictionary,"testingFunctionExpectedBodySensation.csv")

txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_Hasfit.txt"
textLines=getTextLines(txtFilename=txtFilename)
textWords=getTextWords(txtFilename=txtFilename)
fullText=getFullText(txtFilename=txtFilename)
synonymArray=getSynonymArray(["weight","chair","box"])
synonymDictionary=getSynonymDictionary(synonymArray,fullText)
makeSynonymCSV(synonymDictionary,"testingFunctionEquipment.csv")

txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_Hasfit.txt"
textLines=getTextLines(txtFilename=txtFilename)
textWords=getTextWords(txtFilename=txtFilename)
fullText=getFullText(txtFilename=txtFilename)
synonymArray=getSynonymArray(["ready","starting"])
synonymDictionary=getSynonymDictionary(synonymArray,fullText)
makeSynonymCSV(synonymDictionary,"testingFunctionStartWords.csv")

txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_Hasfit.txt"
textLines=getTextLines(txtFilename=txtFilename)
textWords=getTextWords(txtFilename=txtFilename)
fullText=getFullText(txtFilename=txtFilename)
lemmatizeArray=getLemmatizeArray(["over","done"])
synonymArray=getSynonymArray(lemmatizeArray)
synonymArray=getSynonymArray(["over","done"])
synonymDictionary=getSynonymDictionary(synonymArray,fullText)
makeSynonymCSV(synonymDictionary,"video1_stoppingWordCount.csv")
