# Manually obtained phrases

import csv
import os

def codeTextForHTMLHighlighting(originalInputText):
    myWords=originalInputText.split()

    newText=""

    for word in myWords:
        newWord=word[0]+"XYZThisMakesSureHighlightingIsDoneCorrectlyXYZ"+word[1:]+" "
        newText+=newWord

    #remove space at the end
    newText=newText[:-1]
    return newText


def getKeywordsArray(filename):
    keywords = []
    csvfile = open(os.getcwd() + '/Keywords/'+str(filename)+'.csv', encoding="utf-8-sig", mode="r")

    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        keywords.extend(row)

    return keywords

def getColoredHTMLText(fullText,transcriptFilename):
    familiarExercisePhrases = getKeywordsArray("familiarExercisePhrases")
    bodyParts = getKeywordsArray("bodyParts")
    directionToMove = getKeywordsArray("directionToMove")
    expectedBodySensation = getKeywordsArray("expectedBodySensation")
    equipment = getKeywordsArray("equipment")

    startingAnExercise = getKeywordsArray("startingAnExercise")
    stoppingAnExercise = getKeywordsArray("stoppingAnExercise")
    duration = getKeywordsArray("duration")
    pacing = getKeywordsArray("pacing")
    quantityOfAnExercise = getKeywordsArray("quantityOfAnExercise")
    transitioning = getKeywordsArray("transitioning")

    brPhrase = getKeywordsArray("brPhrase")
    encouragingPhrases = getKeywordsArray("encouragingPhrases")
    inaccessibleLocations = getKeywordsArray("inaccessibleLocations")
    subjectivePhrases = getKeywordsArray("subjectivePhrases")
    unfamiliarExercisePhrase = getKeywordsArray("unfamiliarExercisePhrase")

    lightYellow = "#ffeb91"
    lightGreen = "#a1e3aa"
    lightRed = "#f0986c"

    allKeywords = [[brPhrase, lightRed, "brPhrase", "none"],
                   [encouragingPhrases, lightRed, "encouragingPhrases", "none"],
                   [inaccessibleLocations, lightRed, "inaccessibleLocations", "none"],
                   [subjectivePhrases, lightRed, "subjectivePhrases", "none"],
                   [unfamiliarExercisePhrase,lightRed,"unfamiliarExercisePhrase","none"],

                   [startingAnExercise, lightGreen, "startingAnExercise", "before"],
                   [transitioning, lightGreen, "transitioning", "before"],
                   [stoppingAnExercise, lightGreen, "stoppingAnExercise", "after"],
                   [duration, lightGreen, "duration", "none"],
                   [pacing, lightGreen, "pacing", "none"],
                   [quantityOfAnExercise, lightGreen, "quantityOfAnExercise", "none"],

                   [familiarExercisePhrases, lightYellow, "familiarExercisePhrases", "none"],
                   [bodyParts, lightYellow, "bodyParts", "none"],
                   [directionToMove, lightYellow, "directionToMove", "none"],
                   [expectedBodySensation, lightYellow, "expectedBodySensation", "none"],
                   [equipment, lightYellow, "equipment", "none"]]

    colorTextHTML=fullText

    keywordsToIgnore = ["all right", "alright", "right now", "get right into it", "getting right into it",
                        "which one is right for you", "doing it right","matter"]

    for keyword in keywordsToIgnore:
        colorTextHTML = colorTextHTML.replace(" " + keyword,
                                              ' <span style="background-color:#ffffff" class="ignoreThis">' + codeTextForHTMLHighlighting(
                                                  keyword) + '</span>')

    numberOfKeywordsPerClassDictionary = {}

    for keywords in allKeywords:
        count=0

        for keyword in keywords[0]:
            count+=colorTextHTML.count(keyword)
            print(keyword)
            print(colorTextHTML.count(keyword))
            # colorTextHTML = colorTextHTML.replace(" " + keyword,' <span style="background-color:#ffffff" class="' + keywords[2] + '">' + keyword + '</span>')

            if keywords[3]=="none":
                colorTextHTML = colorTextHTML.replace(" "+keyword,' <span style="background-color:#ffffff" class="' + keywords[2] + '">' + codeTextForHTMLHighlighting(keyword) + '</span>')
            elif keywords[3]=="before":
                colorTextHTML = colorTextHTML.replace(" "+keyword,'<br><br><span style="background-color:#ffffff" class="' + keywords[2] + '">' + codeTextForHTMLHighlighting(keyword) + '</span>')
            elif keywords[3]=="after":
                colorTextHTML = colorTextHTML.replace(" "+keyword,' <span style="background-color:#ffffff" class="' + keywords[2] + '">' + codeTextForHTMLHighlighting(keyword) + '</span><br><br>')

        numberOfKeywordsPerClassDictionary[keywords[2]]=count

    # Saving keyword counts to a CSV file
    myKeywordArray = []
    for keywords in allKeywords:
        for i in range(len(keywords[0])):
            keyword = keywords[0][i]
            myKeywordArray.append([keyword, fullText.count(keyword), keywords[2]])

    csvFilename=os.getcwd() + "/Results_Keyword Counts/" + transcriptFilename + "_keywordCount.csv"

    with open(csvFilename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for keyword in myKeywordArray:
            writer.writerow([keyword[0], keyword[1], keyword[2]])

    # colorTextHTMLWithTS = addTimeStamps(colorTextHTML, keywords, 5)  # FIX VARIABLES

    return colorTextHTML, numberOfKeywordsPerClassDictionary

# def addTimeStamps(allKeywords, transcript, vidNum):
#     fileName = os.path.split(os.path.abspath(os.getcwd()))[0] + "/../Video Analysis/Transcripts/video_" + str(
#         vidNum) + "_TimeStampsClean.csv"
#     timestamps = []
#     with open(fileName) as csvFile:
#         csvr = csv.reader(csvFile)
#         timestamps = list(csvr)
#
#     startSearch = 0
#     endSearch = len(transcript)
#     keywordProcessedAlready = {}
#     for keywords in allKeywords:
#         for keyword in keywords[0]:
#             if (keyword in keywordProcessedAlready):
#                 continue
#             else:
#                 keywordProcessedAlready[keyword] = keyword
#             print("++++++++++", keyword)
#             numberOfKeywordsInTranscript = transcript.count(keyword + " ")
#             if numberOfKeywordsInTranscript == 0:
#                 continue
#             keywordLeft = numberOfKeywordsInTranscript
#             timestampsForKeyword = findAllTimestampForKeyword(timestamps, keyword)
#             if numberOfKeywordsInTranscript != len(timestampsForKeyword):
#                 print("number of keywords in transcript doesn't match number of timestamps for the keyword!!!!!",
#                       numberOfKeywordsInTranscript, len(timestampsForKeyword), keyword)
#             timestampIndex = 0  # number of keywords in string
#             while keywordLeft > 0:
#                 wordToBeReplaced = ' ' + keyword + ' '
#                 if keywordLeft < numberOfKeywordsInTranscript:
#                     wordToBeReplaced = keyword + " (" + timestampsForKeyword[keywordLeft][1] + ") "
#                 keywordWithTimestampStr = keyword + " (" + timestampsForKeyword[keywordLeft - 1][
#                     1] + ") "  # find timestamp of keyword from back of timestamps
#                 print("     ", wordToBeReplaced, keywordWithTimestampStr)
#                 transcript = transcript.replace(wordToBeReplaced, keywordWithTimestampStr, keywordLeft)
#                 print("=======", transcript)  # replace instances of keyword with word + timestamp
#                 keywordLeft -= 1
#
#     return transcript
#
#
# def findAllTimestampForKeyword(timestamps, keyword):
#     wordList = keyword.split(' ')
#     timestampsForKeyword = []
#     for i in range(len(timestamps)):
#         if len(wordList) == 1:
#             if keyword == "up":
#                 if timestamps[i][0] != "up":  # has to be exact match
#                     continue
#                 else:
#                     timestampsForKeyword.append(timestamps[i])
#             else:
#                 if keyword in timestamps[i][0]:
#                     timestampsForKeyword.append(timestamps[i])
#         else:
#             matchKeyword = True
#             for j in range(len(wordList)):
#                 if wordList[j] not in timestamps[i + j][0]:
#                     matchKeyword = False
#                     break
#             if matchKeyword == True:
#                 timestampsForKeyword.append(timestamps[i])
#
#     return timestampsForKeyword
