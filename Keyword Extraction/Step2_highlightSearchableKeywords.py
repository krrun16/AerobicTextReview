# Manually obtained phrases

import csv
import os

def codeTextForHTMLHighlighting(originalInputText):
    myWords=originalInputText.split()

    newText=""

    for word in myWords:
        newWord=word[0]+"DoNotReplace"+word[1:]+" "
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

    breathing = getKeywordsArray("breathing")
    encouragingPhrases = getKeywordsArray("encouragingPhrases")
    inaccessibleLocations = getKeywordsArray("inaccessibleLocations")
    subjectivePhrases = getKeywordsArray("subjectivePhrases")

    lightYellow = "#ffeb91"
    lightGreen = "#a1e3aa"
    lightRed = "#f0986c"

    allKeywords = [[breathing, lightRed, "breathing", "none"],
                   [encouragingPhrases, lightRed, "encouragingPhrases", "none"],
                   [inaccessibleLocations, lightRed, "inaccessibleLocations", "none"],
                   [subjectivePhrases, lightRed, "subjectivePhrases", "none"],

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

    for keywords in allKeywords:
        for keyword in keywords[0]:
            # colorTextHTML = colorTextHTML.replace(" " + keyword,' <span style="background-color:#ffffff" class="' + keywords[2] + '">' + keyword + '</span>')

            if keywords[3]=="none":
                colorTextHTML = colorTextHTML.replace(" "+keyword,' <span style="background-color:#ffffff" class="' + keywords[2] + '">' + codeTextForHTMLHighlighting(keyword) + '</span>')
            elif keywords[3]=="before":
                colorTextHTML = colorTextHTML.replace(" "+keyword,'<br><br><span style="background-color:#ffffff" class="' + keywords[2] + '">' + codeTextForHTMLHighlighting(keyword) + '</span>')
            elif keywords[3]=="after":
                colorTextHTML = colorTextHTML.replace(" "+keyword,' <span style="background-color:#ffffff" class="' + keywords[2] + '">' + codeTextForHTMLHighlighting(keyword) + '</span><br><br>')

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

    return colorTextHTML
