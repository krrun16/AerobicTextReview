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
    expectedBodySensation = getKeywordsArray("expectedBodySensation")
    directionToMove = getKeywordsArray("directionToMove")
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
                   [subjectivePhrases, lightRed, "subjectivePhrases", "none"],
                   [unfamiliarExercisePhrase,lightRed,"unfamiliarExercisePhrase","none"],

                   [quantityOfAnExercise, lightGreen, "quantityOfAnExercise", "none"],
                   [startingAnExercise, lightGreen, "startingAnExercise", "before"],
                   [inaccessibleLocations, lightRed, "inaccessibleLocations", "none"],
                   [expectedBodySensation, lightYellow, "expectedBodySensation", "none"],
                   [transitioning, lightGreen, "transitioning", "before"],
                   [duration, lightGreen, "duration", "none"],
                   [stoppingAnExercise, lightGreen, "stoppingAnExercise", "after"],
                   [pacing, lightGreen, "pacing", "none"],


                   [familiarExercisePhrases, lightYellow, "familiarExercisePhrases", "none"],
                   [bodyParts, lightYellow, "bodyParts", "none"],
                   [directionToMove, lightYellow, "directionToMove", "none"],
                   [equipment, lightYellow, "equipment", "none"]]

    colorTextHTML=fullText

    keywordsToIgnore = getKeywordsArray("wordsToIgnore")

    for keyword in keywordsToIgnore:
        colorTextHTML = colorTextHTML.replace(" " + keyword,
                                              ' <span style="background-color:#ffffff" class="ignoreThis">' + codeTextForHTMLHighlighting(
                                                  keyword) + '</span>')

    numberOfKeywordsPerClassDictionary = {}

    for keywords in allKeywords:
        count=0

        for keyword in keywords[0]:
            count+=colorTextHTML.count(keyword)
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

    return colorTextHTML, numberOfKeywordsPerClassDictionary
