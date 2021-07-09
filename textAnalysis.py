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

# function to lemmatize (stem) the original words and then return all possible synonyms
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

# function to lemmatize (stem) the original words and then return all possible noun synonyms
def getLemmatizeArrayNoun(myWords) -> [str]:
    # Lemmatize (getting the stem of a word and it outputs a real word)
    lemmatizer = WordNetLemmatizer()
    myWordsLemm = []
    for word in myWords:
        myWordsLemm.append(lemmatizer.lemmatize(word, pos="n"))
    # Remove duplicate lemmatize results
    myWordsLemm = list(set(myWordsLemm))
    return myWordsLemm

# function to lemmatize (stem) the original words and then return all possible verb synonyms
def getLemmatizeArrayVerb(myWords) -> [str]:
    # Lemmatize (getting the stem of a word and it outputs a real word)
    lemmatizer = WordNetLemmatizer()
    myWordsLemm = []
    for word in myWords:
        myWordsLemm.append(lemmatizer.lemmatize(word, pos="v"))
    # Remove duplicate lemmatize results
    myWordsLemm = list(set(myWordsLemm))
    return myWordsLemm

# function to return all possible synonyms
def getSynonymArray(myWordsLemm) -> [str]:
    # Get synonym
    myWordsSynonym = []
    for word in myWordsLemm:
        for synonym in wordnet.synsets(word):
            for lemma in synonym.lemmas():
                myWordsSynonym.append(lemma.name().replace("_", " "))
    return myWordsSynonym

# function to return noun synonyms
def getSynonymArrayNoun(myWordsLemm) -> [str]:
    # Get synonym
    myWordsSynonym = []
    for word in myWordsLemm:
        for synonym in wordnet.synsets(word, pos="n"):
            for lemma in synonym.lemmas():
                myWordsSynonym.append(lemma.name().replace("_", " "))
    return myWordsSynonym

# function to return verb synonyms
def getSynonymArrayVerb(myWordsLemm) -> [str]:
    # Get synonym
    myWordsSynonym = []
    for word in myWordsLemm:
        for synonym in wordnet.synsets(word, pos="v"):
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

# function that makes a dictionary from an array of manually entered phrases with all parts of speech
def fullGetDictionary(transcriptName,manualArray,csvFilename):
    txtFilename=os.getcwd()+transcriptName
    textLines=getTextLines(txtFilename=txtFilename)
    textWords=getTextWords(txtFilename=txtFilename)
    fullText=getFullText(txtFilename=txtFilename)
    lemmatizeArray=getLemmatizeArray(manualArray)
    synonymArray=getSynonymArray(lemmatizeArray)
    synonymDictionary=getSynonymDictionary(synonymArray,fullText)
    makeSynonymCSV(synonymDictionary,csvFilename+".csv")

# function that makes a dictionary from an array of manually entered phrases with nouns only
def fullGetDictionaryNoun(transcriptName,manualArray,csvFilename):
    txtFilename=os.getcwd()+transcriptName
    textLines=getTextLines(txtFilename=txtFilename)
    textWords=getTextWords(txtFilename=txtFilename)
    fullText=getFullText(txtFilename=txtFilename)
    lemmatizeArray=getLemmatizeArrayNoun(manualArray)
    synonymArray=getSynonymArrayNoun(lemmatizeArray)
    synonymDictionary=getSynonymDictionary(synonymArray,fullText)
    makeSynonymCSV(synonymDictionary,csvFilename+".csv")

# function that makes a dictionary from an array of manually entered phrases with verbs only
def fullGetDictionaryVerb(transcriptName,manualArray,csvFilename):
    txtFilename=os.getcwd()+transcriptName
    textLines=getTextLines(txtFilename=txtFilename)
    textWords=getTextWords(txtFilename=txtFilename)
    fullText=getFullText(txtFilename=txtFilename)
    lemmatizeArray=getLemmatizeArrayVerb(manualArray)
    synonymArray=getSynonymArrayVerb(lemmatizeArray)
    synonymDictionary=getSynonymDictionary(synonymArray,fullText)
    makeSynonymCSV(synonymDictionary,csvFilename+".csv")


# /////////////////////////
# TABLE 1
# manually entered phrases
familiarExercisePhrases=["squat", "jumping jack", "jump", "push up", "plank"]
bodyParts=["arm", "leg", "head", "hand", "foot", "abs", "stomach"]
    # issue: "back" might overlap with direction back?
directionToMove=["up", "down", "left", "right", "side", "front", "back"]
expectedBodySensation=["you should feel a stretch","feel the burn","sore"]
equipment=["weights", "chair","box","mat","ball","resistance band"]

# getting dictionaries
fullGetDictionaryNoun("/Video Analysis/Transcripts/Video_1_Hasfit.txt",
                  familiarExercisePhrases,
                  "video1_FamiliarExercisePhrases")
fullGetDictionaryNoun("/Video Analysis/Transcripts/Video_1_Hasfit.txt",
                  bodyParts,
                  "video1_BodyParts")
fullGetDictionary("/Video Analysis/Transcripts/Video_1_Hasfit.txt",
                  directionToMove,
                  "video1_FunctionDirectionToMove")
fullGetDictionary("/Video Analysis/Transcripts/Video_1_Hasfit.txt",
                  expectedBodySensation,
                  "video1_ExpectedBodySensation")
fullGetDictionaryNoun("/Video Analysis/Transcripts/Video_1_Hasfit.txt",
                  equipment,
                  "video1_Equipment")

# /////////////////////////
# TABLE 3
# manually entered phrases
breathing=["breathe in", "breathe out"]
encouraging=["nice job","I'm so hot","I'm so tired"]
inaccessible=["here","there","make sure you can see the screen"]
filler=["are you ready"]
subjective=["stay nice and under control"]
unfamiliarExercisePhrases=["rise","chop down","stay in line"]

concatenatedUnacceptablePhrases = breathing+encouraging+inaccessible+filler+subjective+unfamiliarExercisePhrases

# getting dictionaries
fullGetDictionary("/Video Analysis/Transcripts/Video_1_Hasfit.txt",
                  concatenatedUnacceptablePhrases,
                  "video1_Unacceptable")
