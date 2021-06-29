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
        for synonym in wordnet.synsets(word.n):
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
    synonymArray=getSynonymArray(manualArray)
    synonymDictionary=getSynonymDictionary(synonymArray,fullText)
    makeSynonymCSV(synonymDictionary,csvFilename+".csv")

# function that makes a dictionary from an array of manually entered phrases with nouns only
def fullGetDictionaryNoun(transcriptName,manualArray,csvFilename):
    txtFilename=os.getcwd()+transcriptName
    textLines=getTextLines(txtFilename=txtFilename)
    textWords=getTextWords(txtFilename=txtFilename)
    fullText=getFullText(txtFilename=txtFilename)
    lemmatizeArray=getLemmatizeArrayNoun(manualArray)
    synonymArray=getSynonymArray(lemmatizeArray)
    synonymArray=getSynonymArray(manualArray)
    synonymDictionary=getSynonymDictionary(synonymArray,fullText)
    makeSynonymCSV(synonymDictionary,csvFilename+".csv")

# function that makes a dictionary from an array of manually entered phrases with verbs only
def fullGetDictionaryVerb(transcriptName,manualArray,csvFilename):
    txtFilename=os.getcwd()+transcriptName
    textLines=getTextLines(txtFilename=txtFilename)
    textWords=getTextWords(txtFilename=txtFilename)
    fullText=getFullText(txtFilename=txtFilename)
    lemmatizeArray=getLemmatizeArrayVerb(manualArray)
    synonymArray=getSynonymArray(lemmatizeArray)
    synonymArray=getSynonymArray(manualArray)
    synonymDictionary=getSynonymDictionary(synonymArray,fullText)
    makeSynonymCSV(synonymDictionary,csvFilename+".csv")


# /////////////////////////
# TABLE 1
# manually entered phrases
familiarExercisePhrases=["squat", "jumping jack", "jump", "push up", "plank"]
bodyParts=["arm", "leg", "head", "hand", "foot", "abs", "stomach"]
    # issue: "back" might overlap with direction back?
directionToMove=["move up","move down", "move left", "move right","move side",
                 "move front", "move back","bring up","bring down","bring left",
                 "bring right","bring side", "bring front","bring back"]
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

# old table 2 code
#txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_Hasfit.txt"
#textLines=getTextLines(txtFilename=txtFilename)
#textWords=getTextWords(txtFilename=txtFilename)
#fullText=getFullText(txtFilename=txtFilename)
#lemmatizeArray=getLemmatizeArray(["ready","starting"])
#synonymArray=getSynonymArray(lemmatizeArray)
#synonymDictionary=getSynonymDictionary(synonymArray,fullText)
#makeSynonymCSV(synonymDictionary,"video1_StartWords.csv")

#txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_Hasfit.txt"
#textLines=getTextLines(txtFilename=txtFilename)
#textWords=getTextWords(txtFilename=txtFilename)
#fullText=getFullText(txtFilename=txtFilename)
#lemmatizeArray=getLemmatizeArray(["over","done"])
#synonymArray=getSynonymArray(lemmatizeArray)
#synonymArray=getSynonymArray(["over","done"])
#synonymDictionary=getSynonymDictionary(synonymArray,fullText)
#makeSynonymCSV(synonymDictionary,"video1_stoppingWordCount.csv")


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


# /////////////////////////
# TABLE 2

# function to count the number of instances of each phrase in the transcript text
def getPhraseDictionary(phraseList,fullText) -> {str:int}:
    myPhraseDictionary = {}
    for phrase in phraseList:
        myPhraseDictionary[phrase] = fullText.count(phrase)

    return myPhraseDictionary

# function to write a dictionary to csv
def makePhraseCSV(phraseDictionaryArray,csvFilename):
    with open(csvFilename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for phraseDictionary in phraseDictionaryArray:
            for key, value in phraseDictionary.items():
                writer.writerow([key, value])

# function to make html text where phrases are highlighted in color. Can use this html text to make a webpage
def getColorText(phraseList,colorValue,fullText,newLine) -> str:
    colorText=fullText
    for phrase in phraseList:
        if newLine=="before":
            colorText=colorText.replace(phrase,
                                        '<br><br><span style="background-color:' + colorValue + '">' + phrase + '</span>')

        elif newLine=="after":
            colorText = colorText.replace(phrase,
                                          '<span style="background-color:' + colorValue + '">' + phrase + '</span><br><br>')

        else:
            colorText = colorText.replace(phrase,
                                          '<span style="background-color:' + colorValue + '">' + phrase + '</span>')

    return colorText

# Manually obtained phrases
startingPhrases=["start",
               "get ready",
                "getting ready",
               "first round"]

stoppingPhrases=["and done",
               "finishing",
               "finished",
               "we're done",
               "are done",
               "be done",
               "is done",
               "it's over",
               "is over"]

durationPhrases=["allotted time period",
               "time period",
               "three two one",
               "three two and one",
               "3 2 1",
               "3 2 & 1",
               "one two",
                "1 2",
               "almost there",
               "almost done",
               " second",
                " minute",
               "time left"]

# will have to write code for the pacing words so that it can detect when multiple instances of words like switch are in close proximity to each other
# pacingWords=["forward forward",
#              "wide arms close arms",
#              "when I say",
#              "switch switch"]

quantityPhrases=["repetition",
               "last one",
               "last time",
               "last round",
               "one more",
               "two more",
               "three more",
               "four more",
               "five more",
               "one time",
               "two times",
               "three times",
               "four times",
               "five times"]

transitionPhrases=["going to",
                 "go over to",
                 "go ahead",
                 "move on",
                 "moving on",
                 "move to",
                 "moving to",
                 "next one",
                 "next up",
                 "we're on to",
                 "we are on to",
                 "repeat",
                 "again",
                 "now we",
                 "another"]

# Getting text information
txtFilename=os.getcwd()+"/Video Analysis/Transcripts/Video_1_HasFit.txt"
textLines=getTextLines(txtFilename=txtFilename)
textWords=getTextWords(txtFilename=txtFilename)
fullText=getFullText(txtFilename=txtFilename)

# Highlighting phrases in color
startingColorOrange="#eb8034"
stoppingYellow="#ebdc34"
durationDarkYellow="#c79d12"
quantityBlue="#a8cce0"
transitionPurple="#c6a8e3"

colorText=getColorText(startingPhrases,startingColorOrange,fullText,newLine="before")
colorText=getColorText(stoppingPhrases,stoppingYellow,colorText,newLine="after")
colorText=getColorText(durationPhrases,durationDarkYellow,colorText,newLine="none")
colorText=getColorText(quantityPhrases,quantityBlue,colorText,newLine="none")
colorText=getColorText(transitionPhrases,transitionPurple,colorText,newLine="before")

# Copy and paste this long string into html file to make a webpage
print(colorText)

# Output CSV with word counts
phraseDictionaryStart=getPhraseDictionary(startingPhrases,fullText)
phraseDictionaryStop=getPhraseDictionary(stoppingPhrases,fullText)
phraseDictionaryDuration=getPhraseDictionary(durationPhrases,fullText)
phraseDictionaryQuantity=getPhraseDictionary(quantityPhrases,fullText)
phraseDictionaryTransition=getPhraseDictionary(transitionPhrases,fullText)

phraseDictionaryArray=[phraseDictionaryStart,
                       phraseDictionaryStop,
                       phraseDictionaryDuration,
                       phraseDictionaryQuantity,
                       phraseDictionaryTransition]

makePhraseCSV(phraseDictionaryArray,"video1phrases_table2.csv")
