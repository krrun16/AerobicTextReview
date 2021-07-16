import csv

def getPercentageSilence(cleanTimestampsFilename):
    cleanTimestampsCSV=open(cleanTimestampsFilename)
    reader = csv.reader(cleanTimestampsCSV)
    allRows=[]

    for row in reader:
        if row[2] != "" and row[3] != "":
            allRows.append([row[0],row[2],row[3]])

    totalTime=allRows[len(allRows)-1][2]

    totalSilence=0
    for i in range(len(allRows)-1):
        try:
            nextFloatNumber=float(allRows[i+1][1])
            firstFloatNumber=float(allRows[i][2])
            totalSilence += nextFloatNumber-firstFloatNumber
        except:
            totalSilence+=0

    print("TOTAL SILENCE: "+str(totalSilence))
    print("TOTAL TIME: " + str(totalTime))
    return round((float(totalSilence)/float(totalTime))*100,2)

import os

# puts () where every silence is so it can be replaced with a highlight later
def addSilencePlaceholders(fullText, vidNum):
    fileName = os.path.split(os.path.abspath(os.getcwd()))[0] + "/Video Analysis/Transcripts/Video_" + str(
        vidNum) + "_TimeStamps.csv"
    timestamps = []
    with open(fileName) as csvFile:
        csvr = csv.reader(csvFile)
        timestamps = list(csvr)
    transcript = fullText.split(" ")
    newTranscript = ""
    pTS = 0 # timestamps pointer, starts at 1 because 0 is the headers
    pTrans = 0 # transcript pointer
    while pTS < len(timestamps)-1 and pTrans < len(transcript)-1:
        wordTS1 = timestamps[pTS][0]
        newTranscript += wordTS1 + " "
        TSSilenceStart = timestamps[pTS][3]
        TSSilenceStop = timestamps[pTS+1][2]
        if len(TSSilenceStart) > 0 and len(TSSilenceStop) > 0:
            if float(TSSilenceStop) - float(TSSilenceStart) > 2: # silence > 2 seconds
                # newTranscript += "() "
                newTranscript += "("+str(int(float(TSSilenceStop) - float(TSSilenceStart)))+" second silence) "
        dashWords = wordTS1.split("-") # takes care of cases like "warm-up" because the time stamp splits it into 2 words
        pTS += len(dashWords)
        pTrans += 1
    return newTranscript
