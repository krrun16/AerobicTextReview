# Manually obtained phrases

import csv
import os

def getKeywordsArray(filename):
    keywords = []
    csvfile = open(os.path.split(os.path.abspath(os.getcwd()))[0] + '/Keywords/'+str(filename)+'.csv', encoding="utf-8-sig", mode="r")

    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        keywords.extend(row)

    return keywords

bodyParts=getKeywordsArray("bodyParts")
directionToMove=getKeywordsArray("directionToMove")
expectedBodySensation=getKeywordsArray("expectedBodySensation")
equipment=getKeywordsArray("equipment")

startingAnExercise=getKeywordsArray("startingAnExercise")
stoppingAnExercise=getKeywordsArray("stoppingAnExercise")
duration=getKeywordsArray("duration")
pacing=getKeywordsArray("pacing")
quantityOfAnExercise=getKeywordsArray("quantityOfAnExercise")
transitioning=getKeywordsArray("transitioning")

breathing=getKeywordsArray("breathing")
encouragingPhrases=getKeywordsArray("encouragingPhrases")
inaccessibleLocations=getKeywordsArray("inaccessibleLocations")
subjectivePhrases=getKeywordsArray("subjectivePhrases")

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

# function to write an array to csv
def makeKeywordCSV(myKeywordArray,csvFilename):
    with open(csvFilename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for keyword in myKeywordArray:
            writer.writerow([keyword[0], keyword[1], keyword[2]])

lightYellow="#ffeb91"
lightGreen="#a1e3aa"
lightRed="#f0986c"

allKeywords=[[bodyParts,lightYellow,"bodyParts","none"],
             [directionToMove,lightYellow,"directionToMove","none"],
             [expectedBodySensation,lightYellow,"expectedBodySensation","none"],
             [equipment,lightYellow,"equipment","none"],
             [startingAnExercise,lightGreen,"startingAnExercise","before"],
             [stoppingAnExercise,lightGreen,"stoppingAnExercise","after"],
             [duration,lightGreen,"duration","none"],
             [pacing,lightGreen,"pacing","none"],
             [quantityOfAnExercise,lightGreen,"quantityOfAnExercise","none"],
             [transitioning,lightGreen,"transitioning","before"],
             [breathing,lightRed,"breathing","none"],
             [encouragingPhrases,lightRed,"encouragingPhrases","none"],
             [inaccessibleLocations,lightRed,"inaccessibleLocations","none"],
             [subjectivePhrases,lightRed,"subjectivePhrases","none"]]

def getColoredHTMLText(fullText):
    colorTextHTML=fullText
    for keywords in allKeywords:
        for keyword in keywords[0]:
            # print(keyword)

            if keywords[3]=="none":
                colorTextHTML = colorTextHTML.replace(" "+keyword,' <span style="background-color:#ffffff" class="' + keywords[2] + '">' + keyword + '</span>')
            elif keywords[3]=="before":
                colorTextHTML = colorTextHTML.replace(" "+keyword,'<br><br><span style="background-color:#ffffff" class="' + keywords[2] + '">' + keyword + '</span>')
            elif keywords[3]=="after":
                colorTextHTML = colorTextHTML.replace(" "+keyword,' <span style="background-color:#ffffff" class="' + keywords[2] + '">' + keyword + '</span><br><br>')

            # if keywords[3]=="none":
            #     colorTextHTML = colorTextHTML.replace(" "+keyword,' <span style="background-color:' + colorValue + '" class="' + keywords[2] + '">' + keyword + '</span>')
            # elif keywords[3]=="before":
            #     colorTextHTML = colorTextHTML.replace(" "+keyword,'<br><br><span style="background-color:' + colorValue + '" class="' + keywords[2] + '">' + keyword + '</span>')
            # elif keywords[3]=="after":
            #     colorTextHTML = colorTextHTML.replace(" "+keyword,' <span style="background-color:' + '" class="' + keywords[2] + '">' + keyword + '</span><br><br>')

    return colorTextHTML

def getKeywordCounts(fullText):
    myKeywordArray = []
    for keywords in allKeywords:
        for i in range(len(keywords[0])):
            keyword = keywords[0][i]
            myKeywordArray.append([keyword,fullText.count(keyword),keywords[2]])

    return myKeywordArray

transcriptFiles=["Video_1_Hasfit.txt",
                 "Video_2_nikeTrainerClub.txt",
                 "Video_3_BodyProject.txt",
                 "Video_4_MadFit.txt",
                 "Video_5_ChloeTing.txt",
                 "Video_6_BeFit.txt"]

from os.path import dirname as up
count=1

for transcriptFilename in transcriptFiles:
    two_up = up(up(up(__file__)))
    txtFilename = two_up + "/Video Analysis/Transcripts/" + transcriptFilename
    fullText = getFullText(txtFilename=txtFilename)
    colorTextHTML = getColoredHTMLText(fullText)
    print(colorTextHTML)
    print()

    myKeywordArray = getKeywordCounts(fullText)
    makeKeywordCSV(myKeywordArray, os.path.split(os.path.abspath(os.getcwd()))[0] + "/Results_Keyword Counts/video"+str(count)+"_keywordCount.csv")
    count+=1
