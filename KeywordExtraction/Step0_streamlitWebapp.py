# STUFF TO INSTALL:
# Python 3.7 (There could be bugs with other versions like 3.8)
# pip install streamlit
# pip install pytube==10.8.5
# pip install youtube_dl
# pip install deepsegment
# pip install tensorflow==1.14
# pip install keras==2.2.5
# pip install nltk

# IMPORTANT IF YOU WANT THE WEB APP TO WORK FOR YOUTUBE LINKS:
# 1) Go to this link, download m3: https://github.com/david-littlefield/pretrained-models/blob/main/gentle/m3
# 2) Go to this link, download k3: https://github.com/david-littlefield/pretrained-models/blob/main/gentle/k3
# 3) Put both of these files into aerobictextreviewLFS/KewywordExtraction/gentle/ext
# 4) Make k3 and m3 executable files:
# For Macs:
# cd into aerobictextreviewLFS/KewywordExtraction/gentle/ext
# Enter: sudo chmod +x k3
# Enter: sudo chmod +x m3

# I'm pretty sure this is how you make files exectuable in PCs but I'm not sure
# For PCs:
# cd into aerobictextreviewLFS/KewywordExtraction/gentle/ext
# Enter: csc k3
# Enter: csc m3

# MORE NOTES:
# 1) If using a YouTube link, the web app will take about 1 min for a 30 min Youtube video
# 2) Run this in terminal to start the app on your computer: streamlit run Step0_streamlitWebapp.py

# /////////////////////////////
from Step1_highlightFillers import *
from Step1a_getTimestampsForYoutube import *
from Step2_annotateSilence import *
from Step3_highlightSearchableKeywords import *

from pytube import YouTube
from os.path import dirname as up
import streamlit as st
import re
import os
import json

st.title("Exercise Text and Audio Analysis")
st.write("Locates 17 categories of exercise instruction phrases and > 2 second silent gaps")
st.write("The goal of this web app is to help exercise instructors improve accessibility of their instructions for people with visual impairments")
st.markdown("____")
page = st.radio("",["Select a Predownloaded Video","Enter a Youtube Link"])

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

myClasses = ["familiarExercisePhrases",
                     "bodyParts",
                     "directionToMove",
                     "expectedBodySensation",
                     "equipment",
                     "startingAnExercise",
                     "stoppingAnExercise",
                     "duration",
                     "pacing",
                     "quantityOfAnExercise",
                     "transitioning",
                     "brPhrase",
                     "encouragingPhrases",
                     "inaccessibleLocations",
                     "filler",
                     "subjectivePhrases",
                     "unfamiliarExercisePhrase",
                    "silences"]

def countNumberOfKeywordsPerClass(colorTextHTML):

    numberOfKeywordsPerClassDictionary={}

    for myClass in myClasses:
        numberOfKeywordsPerClassDictionary[myClass]=colorTextHTML.count('class="'+myClass+'"')

    return numberOfKeywordsPerClassDictionary

if page=="Enter a Youtube Link":
    youtubeLink = st.text_input('Enter an exercise video Youtube link:')
    youtubeLink = youtubeLink.strip()
    print(youtubeLink)

    colorTextHTML = ""
    transcriptText = st.empty()

    @st.cache
    def getColorTextHTML(youtubeLink):
        source = YouTube(youtubeLink)

        try:
            en_caption = source.captions['en']
        except:
            try:
                en_caption = source.captions['a.en']
            except:
                return "<p>The YouTube channel disabled subtitles for this video.</p>", False

        en_caption_convert_to_srt = (en_caption.generate_srt_captions())
        lineTextArray = en_caption_convert_to_srt.splitlines()
        lineTextArray = lineTextArray[2:]

        desired_lines = lineTextArray[::4]

        # save the caption to a file named Output.txt
        text_file = open("YoutubeOutput.txt", "w")
        text_file_gentle = open("gentle/YoutubeOutput.txt", "w")
        fullText = ""
        for lineText in desired_lines:
            fullText += lineText.rstrip('\n') + " "

        fullText = fullText.lower()

        text_file.write(fullText)
        text_file.close()
        text_file_gentle.write(fullText)
        text_file_gentle.close()

        timestampsJson=getTimestampsJsonFromYoutubeLink(youtubeLink)
        os.chdir('..')
        turnTimestampsJsonIntoCSV(timestampsJson)

        # Get the silences included
        fullText = addSilencePlaceholdersForYoutubeVideo(fullText)  # replaces silences with (X second silence) to not disrupt other code

        # Detect fillers, get HTML red highlight
        # highlightedFillers, numberOfFillers = highlightFillersOnText(fullText)

        # Get HTML highlights of the other non-filler keywords
        colorTextHTML, numberOfKeywordsPerClassDictionary = getColoredHTMLText(fullText,
                                                                                "YoutubeOutput.txt")

        colorTextHTML = "<p>" + colorTextHTML + "</p>"
        colorTextHTML = colorTextHTML.replace("XYZThisMakesSureHighlightingIsDoneCorrectlyXYZ", "")

        # Put a span around the silences
        silenceRegex = re.findall(r'\([0-9]+ second silence\)', colorTextHTML)

        noDuplicates = []
        for i in silenceRegex:
            if i not in noDuplicates:
                noDuplicates.append(i)

        for silence in noDuplicates:
            colorTextHTML = colorTextHTML.replace(silence,
                                                    '<span style="background-color:#ffffff" class="silences">' + silence + '</span>')

        return colorTextHTML, True

    # /////////////////////////////
    # Different checkbox options

    st.sidebar.write("Select Categories:")
    st.sidebar.markdown("<b style='background-color:#ffeb91'>Table 1 (specify body movements):</b>",
                        unsafe_allow_html=True)

    placeholder1 = st.sidebar.empty()
    placeholder2 = st.sidebar.empty()
    placeholder3 = st.sidebar.empty()
    placeholder4 = st.sidebar.empty()
    placeholder5 = st.sidebar.empty()

    familiarExercisePhrases = placeholder1.checkbox("Familiar Exercise Phrases", key="a1")
    bodyParts = placeholder2.checkbox("Body Parts", key="a2")
    directionToMove = placeholder3.checkbox("Direction to Move", key="a3")
    expectedBodySensation = placeholder4.checkbox("Expected Body Sensation", key="a4")
    equipment = placeholder5.checkbox("Equipment", key="a5")
    st.sidebar.markdown("____")

    st.sidebar.markdown("<b style='background-color:#a1e3aa'>Table 2 (specify timing):</b>", unsafe_allow_html=True)

    placeholder6 = st.sidebar.empty()
    placeholder7 = st.sidebar.empty()
    placeholder8 = st.sidebar.empty()
    placeholder9 = st.sidebar.empty()
    placeholder10 = st.sidebar.empty()
    placeholder11 = st.sidebar.empty()

    startingAnExercise = placeholder6.checkbox("Starting an Exercise", key="a6")
    stoppingAnExercise = placeholder7.checkbox("Stopping an Exercise", key="a7")
    duration = placeholder8.checkbox("Duration", key="a8")
    pacing = placeholder9.checkbox("Pacing", key="a9")
    quantityOfAnExercise = placeholder10.checkbox("Quantity of an Exercise", key="a10")
    transitioning = placeholder11.checkbox("Transitioning", key="a11")
    st.sidebar.markdown("____")

    st.sidebar.markdown("<b style='background-color:#f0986c'>Table 3 (does not specify movements or timing):</b>",
                        unsafe_allow_html=True)
    placeholder12 = st.sidebar.empty()
    placeholder13 = st.sidebar.empty()
    placeholder14 = st.sidebar.empty()
    placeholder15 = st.sidebar.empty()
    placeholder16 = st.sidebar.empty()
    placeholder17 = st.sidebar.empty()

    brPhrase = placeholder12.checkbox("Breathing", key="a12")
    encouragingPhrases = placeholder13.checkbox("Encouraging Phrases", key="a13")
    inaccessibleLocations = placeholder14.checkbox("Inaccessible Locations", key="a14")
    filler = placeholder15.checkbox("Filler", key="a15")
    subjectivePhrases = placeholder16.checkbox("Subjective Phrases", key="a16")
    unfamiliarExercisePhrase = placeholder17.checkbox("Unfamiliar Exercise Phrase", key="a17")
    st.sidebar.markdown("____")

    st.sidebar.markdown("<b style='background-color:#c2c2c2'>Silences:</b>",
                        unsafe_allow_html=True)
    placeholderTwoSecondSilence = st.sidebar.empty()
    placeholderAverageSilence = st.sidebar.empty()

    twoSecondSilence = placeholderTwoSecondSilence.checkbox("2 Second or Greater Silences", key="twoSecond")

    if youtubeLink:
        transcriptText.empty()

        colorTextHTML, didItWork = getColorTextHTML(youtubeLink)
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

        if didItWork:
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTML)

            percentageSilence = getPercentageSilence(os.getcwd() + "/YoutubeOutput_timestamps.csv")
            placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
                                               unsafe_allow_html=True)

            # Update the checkbox itself
            twoSecondSilence = placeholderTwoSecondSilence.checkbox("2 Second or Greater Silences (" + str(numberOfKeywordsPerClassDictionary["silences"]) + ")", key="d0")

            familiarExercisePhrases = placeholder1.checkbox("Familiar Exercise Phrases (" + str(numberOfKeywordsPerClassDictionary["familiarExercisePhrases"]) + ")",key="c1")
            bodyParts = placeholder2.checkbox("Body Parts (" + str(numberOfKeywordsPerClassDictionary["bodyParts"]) + ")",key="c2")
            directionToMove = placeholder3.checkbox("Direction to Move (" + str(numberOfKeywordsPerClassDictionary["directionToMove"]) + ")", key="c3")
            expectedBodySensation = placeholder4.checkbox("Expected Body Sensation (" + str(numberOfKeywordsPerClassDictionary["expectedBodySensation"]) + ")",key="c4")
            equipment = placeholder5.checkbox("Equipment (" + str(numberOfKeywordsPerClassDictionary["equipment"]) + ")",key="c5")

            startingAnExercise = placeholder6.checkbox("Starting an Exercise (" + str(numberOfKeywordsPerClassDictionary["startingAnExercise"]) + ")", key="c6")
            stoppingAnExercise = placeholder7.checkbox("Stopping an Exercise (" + str(numberOfKeywordsPerClassDictionary["stoppingAnExercise"]) + ")", key="c7")
            duration = placeholder8.checkbox("Duration (" + str(numberOfKeywordsPerClassDictionary["duration"]) + ")", key="c8")
            pacing = placeholder9.checkbox("Pacing (" + str(numberOfKeywordsPerClassDictionary["pacing"]) + ")", key="c9")
            quantityOfAnExercise = placeholder10.checkbox("Quantity of an Exercise (" + str(numberOfKeywordsPerClassDictionary["quantityOfAnExercise"]) + ")",key="c10")
            transitioning = placeholder11.checkbox("Transitioning (" + str(numberOfKeywordsPerClassDictionary["transitioning"]) + ")", key="c11")

            brPhrase = placeholder12.checkbox("Breathing (" + str(numberOfKeywordsPerClassDictionary["brPhrase"]) + ")", key="c12")
            encouragingPhrases = placeholder13.checkbox("Encouraging Phrases (" + str(numberOfKeywordsPerClassDictionary["encouragingPhrases"]) + ")", key="c13")
            inaccessibleLocations = placeholder14.checkbox("Inaccessible Locations (" + str(numberOfKeywordsPerClassDictionary["inaccessibleLocations"]) + ")",key="c14")
            filler = placeholder15.checkbox("Filler (" + str(numberOfKeywordsPerClassDictionary["filler"]) + ")", key="c15")
            subjectivePhrases = placeholder16.checkbox("Subjective Phrases (" + str(numberOfKeywordsPerClassDictionary["subjectivePhrases"]) + ")", key="c16")
            unfamiliarExercisePhrase = placeholder17.checkbox("Unfamiliar Exercise Phrases (" + str(numberOfKeywordsPerClassDictionary["unfamiliarExercisePhrase"]) + ")",key="c17")

    # /////////////////////////////
    # Changes the highlight colors when checkboxes are pressed
    lightGrey = "#c2c2c2"
    lightYellow = "#ffeb91"
    lightGreen = "#a1e3aa"
    lightRed = "#f0986c"

    # Table 1
    if twoSecondSilence:
        colorTextHTML = colorTextHTML.replace(
            '<span style="background-color:#ffffff" class="silences">',
            '<span style="background-color:' + str(lightGrey) + '" class="silences">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if familiarExercisePhrases:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="familiarExercisePhrases">',
                                              '<span style="background-color:' + str(
                                                  lightYellow) + '" class="familiarExercisePhrases">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if bodyParts:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="bodyParts">',
                                              '<span style="background-color:' + str(
                                                  lightYellow) + '" class="bodyParts">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if directionToMove:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="directionToMove">',
                                              '<span style="background-color:' + str(
                                                  lightYellow) + '" class="directionToMove">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if expectedBodySensation:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="expectedBodySensation">',
                                              '<span style="background-color:' + str(
                                                  lightYellow) + '" class="expectedBodySensation">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if equipment:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="equipment">',
                                              '<span style="background-color:' + str(
                                                  lightYellow) + '" class="equipment">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    # /////////////////////////////
    # Table 2

    if startingAnExercise:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="startingAnExercise">',
                                              '<span style="background-color:' + str(
                                                  lightGreen) + '" class="startingAnExercise">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if stoppingAnExercise:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="stoppingAnExercise">',
                                              '<span style="background-color:' + str(
                                                  lightGreen) + '" class="stoppingAnExercise">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if duration:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="duration">',
                                              '<span style="background-color:' + str(
                                                  lightGreen) + '" class="duration">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if pacing:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="pacing">',
                                              '<span style="background-color:' + str(lightGreen) + '" class="pacing">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if quantityOfAnExercise:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="quantityOfAnExercise">',
                                              '<span style="background-color:' + str(
                                                  lightGreen) + '" class="quantityOfAnExercise">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if transitioning:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="transitioning">',
                                              '<span style="background-color:' + str(
                                                  lightGreen) + '" class="transitioning">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    # /////////////////////////////
    # Table 3

    if brPhrase:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="brPhrase">',
                                              '<span style="background-color:' + str(lightRed) + '" class="brPhrase">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if encouragingPhrases:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="encouragingPhrases">',
                                              '<span style="background-color:' + str(
                                                  lightRed) + '" class="encouragingPhrases">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if inaccessibleLocations:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="inaccessibleLocations">',
                                              '<span style="background-color:' + str(
                                                  lightRed) + '" class="inaccessibleLocations">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if filler:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="filler">',
                                              '<span style="background-color:' + str(lightRed) + '" class="filler">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if subjectivePhrases:
        colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="subjectivePhrases">',
                                              '<span style="background-color:' + str(
                                                  lightRed) + '" class="subjectivePhrases">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    if unfamiliarExercisePhrase:
        colorTextHTML = colorTextHTML.replace(
            '<span style="background-color:#ffffff" class="unfamiliarExercisePhrase">',
            '<span style="background-color:' + str(lightRed) + '" class="unfamiliarExercisePhrase">')
        transcriptText.empty()
        transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)
else:
    myClasses = ["familiarExercisePhrases",
                 "bodyParts",
                 "directionToMove",
                 "expectedBodySensation",
                 "equipment",
                 "startingAnExercise",
                 "stoppingAnExercise",
                 "duration",
                 "pacing",
                 "quantityOfAnExercise",
                 "transitioning",
                 "brPhrase",
                 "encouragingPhrases",
                 "inaccessibleLocations",
                 "filler",
                 "subjectivePhrases",
                 "unfamiliarExercisePhrase",
                 "silences"]

    videoList = ["", "Video 1 HASFit", "Video 2 NTC", "Video 3 BodyProject", "Video 4 MadFit", "Video 5 CT","Video 6 BeFit","Video 7 OrangeTheory","Video 8 Fitness Blender", "Video 9 HIIT", "Video 10 BodyBuilder (Extra for unofficial testing)"]
    videoSelected = st.selectbox("Select a predownloaded video:", videoList)

    colorTextHTMLa = ""
    transcriptTexta = st.empty()

    @st.cache
    def getColorHTMLNoYoutube(transcriptFilenameShort,timestampsFilenameShort, videoNumber):
        one_up = up(up(__file__))
        txtFilename = one_up + "/Video Analysis/Transcripts/" + transcriptFilenameShort

        # Get the silences included
        fullText=getFullText(txtFilename)

        fullText = addSilencePlaceholders(fullText, videoNumber)  # replaces silences with () to not disrupt other code

        # Detect fillers, get HTML red highlight
        highlightedFillers, numberOfFillers = highlightFillersOnText(fullText)

        # Get HTML highlights of the other non-filler keywords
        colorTextHTMLa, numberOfKeywordsPerClassDictionary = getColoredHTMLText(highlightedFillers,transcriptFilenameShort)

        colorTextHTMLa = "<p>" + colorTextHTMLa + "</p>"
        colorTextHTMLa = colorTextHTMLa.replace("XYZThisMakesSureHighlightingIsDoneCorrectlyXYZ", "")

        #Put a span around the silences
        silenceRegex = re.findall(r'\([0-9]+ second silence\)',colorTextHTMLa)

        noDuplicates = []
        for i in silenceRegex:
            if i not in noDuplicates:
                noDuplicates.append(i)

        for silence in noDuplicates:
            colorTextHTMLa=colorTextHTMLa.replace(silence,'<span style="background-color:#ffffff" class="silences">'+silence+'</span>')

        return colorTextHTMLa

    # /////////////////////////////
    # Different checkbox options

    st.sidebar.write("Select Categories:")
    st.sidebar.markdown("<b style='background-color:#ffeb91'>Table 1 (specify body movements):</b>",
                        unsafe_allow_html=True)

    placeholder1a = st.sidebar.empty()
    placeholder2a = st.sidebar.empty()
    placeholder3a = st.sidebar.empty()
    placeholder4a = st.sidebar.empty()
    placeholder5a = st.sidebar.empty()

    familiarExercisePhrasesa = placeholder1a.checkbox("Familiar Exercise Phrases", key="b1")
    bodyPartsa = placeholder2a.checkbox("Body Parts", key="b2")
    directionToMovea = placeholder3a.checkbox("Direction to Move", key="b3")
    expectedBodySensationa = placeholder4a.checkbox("Expected Body Sensation", key="b4")
    equipmenta = placeholder5a.checkbox("Equipment", key="b5")
    st.sidebar.markdown("____")

    st.sidebar.markdown("<b style='background-color:#a1e3aa'>Table 2 (specify timing):</b>", unsafe_allow_html=True)

    placeholder6a = st.sidebar.empty()
    placeholder7a = st.sidebar.empty()
    placeholder8a = st.sidebar.empty()
    placeholder9a = st.sidebar.empty()
    placeholder10a = st.sidebar.empty()
    placeholder11a = st.sidebar.empty()

    startingAnExercisea = placeholder6a.checkbox("Starting an Exercise", key="b6")
    stoppingAnExercisea = placeholder7a.checkbox("Stopping an Exercise", key="b7")
    durationa = placeholder8a.checkbox("Duration", key="b8")
    pacinga = placeholder9a.checkbox("Pacing", key="b9")
    quantityOfAnExercisea = placeholder10a.checkbox("Quantity of an Exercise", key="b10")
    transitioninga = placeholder11a.checkbox("Transitioning", key="b11")
    st.sidebar.markdown("____")

    st.sidebar.markdown("<b style='background-color:#f0986c'>Table 3 (does not specify movements or timing):</b>",
                        unsafe_allow_html=True)
    placeholder12a = st.sidebar.empty()
    placeholder13a = st.sidebar.empty()
    placeholder14a = st.sidebar.empty()
    placeholder15a = st.sidebar.empty()
    placeholder16a = st.sidebar.empty()
    placeholder17a = st.sidebar.empty()

    brPhrasea = placeholder12a.checkbox("Breathing", key="b12")
    encouragingPhrasesa = placeholder13a.checkbox("Encouraging Phrases", key="b13")
    inaccessibleLocationsa = placeholder14a.checkbox("Inaccessible Locations", key="b14")
    fillera = placeholder15a.checkbox("Filler", key="b15")
    subjectivePhrasesa = placeholder16a.checkbox("Subjective Phrases", key="b16")
    unfamiliarExercisePhrasea = placeholder17a.checkbox("Unfamiliar Exercise Phrase", key="b17")

    st.sidebar.markdown("____")
    st.sidebar.markdown("<b style='background-color:#c2c2c2'>Silences:</b>",
                        unsafe_allow_html=True)
    placeholderTwoSecondSilence = st.sidebar.empty()
    placeholderAverageSilence = st.sidebar.empty()

    twoSecondSilence = placeholderTwoSecondSilence.checkbox("2 Second or Greater Silences", key="twoSecond")


    # Runs text analysis when new video selected
    if videoSelected:
        transcriptTexta.empty()

        numberOfKeywordsPerClassDictionary = {}

        if videoSelected == "Video 1 HASFit":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_1_TimeStamps.csv"
            percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            placeholderAverageSilence.markdown("<p>"+str(percentageSilence)+"% of the audio was silence</p>",unsafe_allow_html=True)

            videoNumber = 1
            transcriptFilenameShort = "Video_1_Hasfit.txt"
            timestampsFilenameShort = "Video_1_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort,timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        elif videoSelected == "Video 2 NTC":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_2_TimeStamps.csv"
            percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
                                               unsafe_allow_html=True)

            videoNumber = 2
            transcriptFilenameShort = "Video_2_nikeTrainerClub.txt"
            timestampsFilenameShort = "Video_2_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort, timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        elif videoSelected == "Video 3 BodyProject":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_3_TimeStamps.csv"
            percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
                                               unsafe_allow_html=True)

            videoNumber = 3
            transcriptFilenameShort = "Video_3_BodyProject.txt"
            timestampsFilenameShort = "Video_3_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort, timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        elif videoSelected == "Video 4 MadFit":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_4_TimeStamps.csv"
            percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
                                               unsafe_allow_html=True)

            videoNumber = 4
            transcriptFilenameShort = "Video_4_MadFit.txt"
            timestampsFilenameShort = "Video_4_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort, timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        elif videoSelected == "Video 5 CT":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_5_TimeStamps.csv"
            percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
                                               unsafe_allow_html=True)

            videoNumber = 5
            transcriptFilenameShort = "Video_5_ChloeTing.txt"
            timestampsFilenameShort = "Video_5_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort, timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        elif videoSelected == "Video 6 BeFit":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_6_TimeStamps.csv"
            percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
                                               unsafe_allow_html=True)

            videoNumber = 6
            transcriptFilenameShort = "Video_6_BeFit.txt"
            timestampsFilenameShort = "Video_6_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort, timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        elif videoSelected == "Video 7 OrangeTheory":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_7_TimeStamps.csv"
            percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
                                               unsafe_allow_html=True)

            videoNumber = 7
            transcriptFilenameShort = "Video_7_OrangeTheory.txt"
            timestampsFilenameShort = "Video_7_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort, timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        elif videoSelected == "Video 8 Fitness Blender":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_8_TimeStamps.csv"
            percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
                                               unsafe_allow_html=True)

            videoNumber = 8
            transcriptFilenameShort = "Video_8_FitnessBlender.txt"
            timestampsFilenameShort = "Video_8_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort, timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        elif videoSelected == "Video 9 HIIT":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_9_TimeStamps.csv"
            percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
                                               unsafe_allow_html=True)

            videoNumber = 9
            transcriptFilenameShort = "Video_9_HIIT.txt"
            timestampsFilenameShort = "Video_9_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort, timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        elif videoSelected == "Video 10 BodyBuilder (Extra for unofficial testing)":
            one_up = up(up(__file__))
            cleanTimestampsFilename = one_up + "/Video Analysis/Transcripts/Video_10_TimeStamps.csv"
            # percentageSilence = getPercentageSilence(cleanTimestampsFilename)
            # placeholderAverageSilence.markdown("<p>" + str(percentageSilence) + "% of the audio was silence</p>",
            #                                    unsafe_allow_html=True)

            videoNumber = 10
            transcriptFilenameShort = "Video_10_Bodybuilder.txt"
            timestampsFilenameShort = "Video_10_TimeStamps.csv"
            colorTextHTMLa = getColorHTMLNoYoutube(transcriptFilenameShort, timestampsFilenameShort, videoNumber)
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
            numberOfKeywordsPerClassDictionary = countNumberOfKeywordsPerClass(colorTextHTMLa)

        if all(name in numberOfKeywordsPerClassDictionary for name in myClasses):
            # Update the checkbox itself

            twoSecondSilence = placeholderTwoSecondSilence.checkbox("2 Second or Greater Silences (" + str(numberOfKeywordsPerClassDictionary["silences"]) + ")", key="d0")

            familiarExercisePhrasesa = placeholder1a.checkbox("Familiar Exercise Phrases (" + str(numberOfKeywordsPerClassDictionary["familiarExercisePhrases"]) + ")", key="d1")
            bodyPartsa = placeholder2a.checkbox("Body Parts (" + str(numberOfKeywordsPerClassDictionary["bodyParts"]) + ")", key="d2")
            directionToMovea = placeholder3a.checkbox("Direction to Move (" + str(numberOfKeywordsPerClassDictionary["directionToMove"]) + ")", key="d3")
            expectedBodySensationa = placeholder4a.checkbox("Expected Body Sensation (" + str(numberOfKeywordsPerClassDictionary["expectedBodySensation"]) + ")",key="d4")
            equipmenta = placeholder5a.checkbox("Equipment (" + str(numberOfKeywordsPerClassDictionary["equipment"]) + ")", key="d5")

            startingAnExercisea = placeholder6a.checkbox("Starting an Exercise (" + str(numberOfKeywordsPerClassDictionary["startingAnExercise"]) + ")",key="d6")
            stoppingAnExercisea = placeholder7a.checkbox("Stopping an Exercise (" + str(numberOfKeywordsPerClassDictionary["stoppingAnExercise"]) + ")",key="d7")
            durationa = placeholder8a.checkbox("Duration (" + str(numberOfKeywordsPerClassDictionary["duration"]) + ")", key="d8")
            pacinga = placeholder9a.checkbox("Pacing (" + str(numberOfKeywordsPerClassDictionary["pacing"]) + ")", key="d9")
            quantityOfAnExercisea = placeholder10a.checkbox("Quantity of an Exercise (" + str(numberOfKeywordsPerClassDictionary["quantityOfAnExercise"]) + ")",key="d10")
            transitioninga = placeholder11a.checkbox("Transitioning (" + str(numberOfKeywordsPerClassDictionary["transitioning"]) + ")", key="d11")

            brPhrasea = placeholder12a.checkbox("Breathing (" + str(numberOfKeywordsPerClassDictionary["brPhrase"]) + ")", key="d12")
            encouragingPhrasesa = placeholder13a.checkbox("Encouraging Phrases (" + str(numberOfKeywordsPerClassDictionary["encouragingPhrases"]) + ")",key="d13")
            inaccessibleLocationsa = placeholder14a.checkbox("Inaccessible Locations (" + str(numberOfKeywordsPerClassDictionary["inaccessibleLocations"]) + ")",key="d14")
            fillera = placeholder15a.checkbox("Filler (" + str(numberOfKeywordsPerClassDictionary["filler"]) + ")", key="d15")
            subjectivePhrasesa = placeholder16a.checkbox("Subjective Phrases (" + str(numberOfKeywordsPerClassDictionary["subjectivePhrases"]) + ")", key="d16")
            unfamiliarExercisePhrasea = placeholder17a.checkbox("Unfamiliar Exercise Phrases (" + str(numberOfKeywordsPerClassDictionary["unfamiliarExercisePhrase"]) + ")", key="d17")

        # /////////////////////////////
        # Changes the highlight colors when checkboxes are pressed
        lightGrey = "#c2c2c2"
        lightYellow = "#ffeb91"
        lightGreen = "#a1e3aa"
        lightRed = "#f0986c"

        if twoSecondSilence:
            colorTextHTMLa = colorTextHTMLa.replace(
                '<span style="background-color:#ffffff" class="silences">',
                '<span style="background-color:' + str(
                    lightGrey) + '" class="silences">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        # Table 1

        if familiarExercisePhrasesa:
            colorTextHTMLa = colorTextHTMLa.replace(
                '<span style="background-color:#ffffff" class="familiarExercisePhrases">',
                '<span style="background-color:' + str(
                    lightYellow) + '" class="familiarExercisePhrases">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if bodyPartsa:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="bodyParts">',
                                                  '<span style="background-color:' + str(
                                                      lightYellow) + '" class="bodyParts">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if directionToMovea:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="directionToMove">',
                                                  '<span style="background-color:' + str(
                                                      lightYellow) + '" class="directionToMove">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if expectedBodySensationa:
            colorTextHTMLa = colorTextHTMLa.replace(
                '<span style="background-color:#ffffff" class="expectedBodySensation">',
                '<span style="background-color:' + str(
                    lightYellow) + '" class="expectedBodySensation">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if equipmenta:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="equipment">',
                                                  '<span style="background-color:' + str(
                                                      lightYellow) + '" class="equipment">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        # /////////////////////////////
        # Table 2

        if startingAnExercisea:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="startingAnExercise">',
                                                  '<span style="background-color:' + str(
                                                      lightGreen) + '" class="startingAnExercise">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if stoppingAnExercisea:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="stoppingAnExercise">',
                                                  '<span style="background-color:' + str(
                                                      lightGreen) + '" class="stoppingAnExercise">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if durationa:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="duration">',
                                                  '<span style="background-color:' + str(
                                                      lightGreen) + '" class="duration">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if pacinga:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="pacing">',
                                                  '<span style="background-color:' + str(
                                                      lightGreen) + '" class="pacing">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if quantityOfAnExercisea:
            colorTextHTMLa = colorTextHTMLa.replace(
                '<span style="background-color:#ffffff" class="quantityOfAnExercise">',
                '<span style="background-color:' + str(
                    lightGreen) + '" class="quantityOfAnExercise">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if transitioninga:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="transitioning">',
                                                  '<span style="background-color:' + str(
                                                      lightGreen) + '" class="transitioning">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        # /////////////////////////////
        # Table 3

        if brPhrasea:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="brPhrase">',
                                                  '<span style="background-color:' + str(
                                                      lightRed) + '" class="brPhrase">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if encouragingPhrasesa:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="encouragingPhrases">',
                                                  '<span style="background-color:' + str(
                                                      lightRed) + '" class="encouragingPhrases">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if inaccessibleLocationsa:
            colorTextHTMLa = colorTextHTMLa.replace(
                '<span style="background-color:#ffffff" class="inaccessibleLocations">',
                '<span style="background-color:' + str(
                    lightRed) + '" class="inaccessibleLocations">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if fillera:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="filler">',
                                                  '<span style="background-color:' + str(
                                                      lightRed) + '" class="filler">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if subjectivePhrasesa:
            colorTextHTMLa = colorTextHTMLa.replace('<span style="background-color:#ffffff" class="subjectivePhrases">',
                                                  '<span style="background-color:' + str(
                                                      lightRed) + '" class="subjectivePhrases">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)

        if unfamiliarExercisePhrasea:
            colorTextHTMLa = colorTextHTMLa.replace(
                '<span style="background-color:#ffffff" class="unfamiliarExercisePhrase">',
                '<span style="background-color:' + str(lightRed) + '" class="unfamiliarExercisePhrase">')
            transcriptTexta.empty()
            transcriptTexta.markdown(colorTextHTMLa, unsafe_allow_html=True)
