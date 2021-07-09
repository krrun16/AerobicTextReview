# Manually obtained phrases
bodyParts=["muscle",
"abs",
'lower body',
"tricep",
"heel",
"glut",
'back',
'upper body',
"arm",
"feet",
"knee",
"hip",
"shoulder",
"core",
"palm",
"pinkie",
"bicep",
"elbow",
"upper arm",
"glute",
"ear",
"forearm",
"finger",
"rib",
"tail",
"calf",
"calves"]

directionToMove=["on the ground",
"up",
"back",
"angle",
"to the ground",
"down",
"below",
"over",
"parallel",
"ground",
"off the ground",
"back down",
"high",
"straight up",
"in line",
"at the top",
"side to side",
"open",
"back together",
"forward",
"around",
"into",
"straight",
"side",
"right",
"other side",
"lower",
"low",
"in the ground",
"out",
"left",
"center",
"degrees",
"front",
"hip level",
"toward",
"above",
"straight line",
"higher"]

equipment=["weight",
"dumbbell",
"box",
"chair",
"seat",
"water",
"mat",
"towel",
"jump rope"]

startingAnExercise=["getting ready",
"we're starting",
"starting",
"getting right into it",
"get right into it",
"first we're",
'start off',
"start it",
"the first exercise",
"start with",
"start our stretch",
"first workout",
"here we go",
"you ready",
"join me now",
"starting off",
"start to"]

stoppingAnExercise=["we are done",
"are done",
"we're done",
"it's over",
"done okay",
"it is done",
"is done",
"that's the end"]

duration=["not done yet",
"not much left",
"halfway done",
"got ten seconds",
"ten second",
"got 10 more seconds",
"10 more seconds",
"more seconds left",
"more seconds",
"second break",
'20 second',
"30 second",
"seconds here",
"twenty seconds",
"ten seconds",
"we have five seconds",
"work for 20 seconds",
"twenty second",
"we've got 40 seconds",
"20 seconds",
"40 seconds of work",
"40 second",
"forty seconds here",
"forty second",
"40 seconds",
"20 seconds of each",
"60 seconds",
"20 seconds of",
"last 60 seconds",
"almost done",
"five more seconds",
"not much time left",
"almost there",
"we are almost there",
"can see the finish line",
"not done yet",
"getting close to the end,",
"seconds"]

pacing=["as quick as we can",
"four three two one",
"three two one",
"five four three two one",
"four three two one zero",
"five four three two one zero",
"four three two one and zero",
"three two one and zero",
"five four three two and one",
"five four three two and last one zero",
"allotted time period",
"five come on four three two one",
"speed this up",
"last four three two one",
"cue you down",
"four three",
"two one",
"in three two one",
"in three two one",
"five come on four three two one",
"three two",
"at your own pace",
"slow slow slow",
"switch switch switch",
"speed it up",
"good tempo",
"go in a tempo",
"side side",
"at my counts",
"fast",
"three in two and in one",
"the pace is high",
"go slow",
"go fast",
"three two and one",
"in three two and one",
"3 2 1",
"in three come on in two and one",
"three two and one",
"3 2 & 1",
"two and one",
"three come on two and one",
"three come on two one",
"don't rush",
"fast pace",
"two and again one",
"fast as you can",
"your pace",
"slow right down",
"one two",
"moving at a pace",
"pause whenever",
"take a break whenever",
"break whenever",
"do it slow"]

quantityOfAnExercise=["one more time",
"not many left",
"don't have much left",
"one more exercise",
"few more",
"last one",
"few times",
"two times",
"two more",
"three different moves",
"three times",
"last five",
"one more set",
"three more",
"three rounds",
"try that again",
"one more",
"two different movement",
"last round",
"one more round",
"last time",
"two jumping jack",
"four high knee",
"one on each side",
"one right and one left",
"circuit number",
"last time on",
"this is one of two"]

transitioning=["round one",
"then we go to",
"we're going to",
"right into the",
"going into our",
"another combo",
"into the next",
"going back to",
"we're going to go",
"we're going back",
"we're changing",
"then you're",
"we're gonna",
"we're back to",
"we're gonna go to",
"we're going to go back",
"now I want you to",
"it's time for",
"we're gonna do",
"we've got another",
"then we'll go",
"now we're going",
"no we're going up",
"march now",
"then we'll",
"we'll take it to",
"no we're going",
"we're going into",
"we're moving into",
"gonna move straight into",
"it's coming next",
"we're gonna go",
"then I",
"we're doing",
"we've got some",
"and we're straight in",
"then get up",
"do another",
"switch side",
"let's do",
"switch sides",
"we are headed to",
"head to"]

breathing=["breathe",
"inhales",
"exhales",
"inhale",
"exhale",
"catch your breath",
"big inhale",
"big exhale",
"slow exhales",
"breather",
"big breathes",
"deep breaths",
"keep breathing"]

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
             [equipment,lightYellow,"equipment","none"],
             [startingAnExercise,lightGreen,"startingAnExercise","before"],
             [stoppingAnExercise,lightGreen,"stoppingAnExercise","after"],
             [duration,lightGreen,"duration","none"],
             [pacing,lightGreen,"pacing","none"],
             [quantityOfAnExercise,lightGreen,"quantityOfAnExercise","none"],
             [transitioning,lightGreen,"transitioning","before"],
             [breathing,lightRed,"breathing","none"]]

def getColoredHTMLText(fullText):
    colorTextHTML=fullText
    for keywords in allKeywords:
        for keyword in keywords[0]:
            print(keyword)

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

def getKeywordCounts():
    myKeywordArray = []
    for keywords in allKeywords:
        for i in range(len(keywords[0])):
            keyword = keywords[0][i]
            myKeywordArray.append([keyword,fullText.count(keyword),keywords[2]])

    return myKeywordArray

# Video_1_Hasfit.txt
# Video_2_nikeTrainerClub.txt
# Video_3_BodyProject.txt
# Video_4_MadFit.txt
# Video_5_ChloeTing.txt
# Video_6_BeFit.txt

# CHANGE THE FILENAME HERE
txtFilename=os.path.split(os.path.abspath(os.getcwd()))[0]+"/Video Analysis/Transcripts/Video_6_BeFit.txt"

textLines=getTextLines(txtFilename=txtFilename)
textWords=getTextWords(txtFilename=txtFilename)
fullText=getFullText(txtFilename=txtFilename)
colorTextHTML=getColoredHTMLText(fullText)

# Copy and paste this long string into html file to make a webpage
print(colorTextHTML)

# Output CSV with word counts
myKeywordArray=getKeywordCounts()

# CHANGE THE FILENAME HERE
makeKeywordCSV(myKeywordArray,os.getcwd()+"/Keyword Counts/video6_keywordCount.csv")
