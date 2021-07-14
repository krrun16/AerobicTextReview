# Stuff to install:

# pip install streamlit
# pip install pytube3

# Run this in terminal to start the app on your computer: streamlit run Step0_streamlitWebapp.py

# /////////////////////////////
import streamlit as st
st.title("Exercise Transcript Analysis")
st.write("Identifies 17 different classes of exercise transcript phrases")

# /////////////////////////////
# Different checkbox options

st.sidebar.write("Select Classes:")
st.sidebar.markdown("<b style='background-color:#ffeb91'>Table 1 (specify body movements):</b>", unsafe_allow_html=True)

placeholder1 = st.sidebar.empty()
placeholder2 = st.sidebar.empty()
placeholder3 = st.sidebar.empty()
placeholder4 = st.sidebar.empty()
placeholder5 = st.sidebar.empty()

familiarExercisePhrases = placeholder1.checkbox("Familiar Exercise Phrases")
bodyParts = placeholder2.checkbox("Body Parts")
directionToMove = placeholder3.checkbox("Direction to Move")
expectedBodySensation = placeholder4.checkbox("Expected Body Sensation")
equipment = placeholder5.checkbox("Equipment")
st.sidebar.markdown("____")

st.sidebar.markdown("<b style='background-color:#a1e3aa'>Table 2 (specify timing):</b>", unsafe_allow_html=True)

placeholder6 = st.sidebar.empty()
placeholder7 = st.sidebar.empty()
placeholder8 = st.sidebar.empty()
placeholder9 = st.sidebar.empty()
placeholder10 = st.sidebar.empty()
placeholder11 = st.sidebar.empty()

startingAnExercise = placeholder6.checkbox("Starting an Exercise")
stoppingAnExercise = placeholder7.checkbox("Stopping an Exercise")
duration = placeholder8.checkbox("Duration")
pacing = placeholder9.checkbox("Pacing")
quantityOfAnExercise = placeholder10.checkbox("Quantity of an Exercise")
transitioning = placeholder11.checkbox("Transitioning")
st.sidebar.markdown("____")

st.sidebar.markdown("<b style='background-color:#f0986c'>Table 3 (does not specify movements or time):</b>", unsafe_allow_html=True)
placeholder12 = st.sidebar.empty()
placeholder13 = st.sidebar.empty()
placeholder14 = st.sidebar.empty()
placeholder15 = st.sidebar.empty()
placeholder16 = st.sidebar.empty()
placeholder17 = st.sidebar.empty()

brPhrase = placeholder12.checkbox("Breathing")
encouragingPhrases = placeholder13.checkbox("Encouraging Phrases")
inaccessibleLocations = placeholder14.checkbox("Inaccessible Locations")
filler = placeholder15.checkbox("Filler")
subjectivePhrases = placeholder16.checkbox("Subjective Phrases")
unfamiliarExercisePhrase = placeholder17.checkbox("Unfamiliar Exercise Phrase")

# /////////////////////////////
# Upload a youtube link
youtubeLink = st.text_input('Youtube Link:')

from Step1_highlightFillers import *
from Step2_highlightSearchableKeywords import *

from pytube import YouTube

@st.cache
def getColorTextHTML(youtubeLink):
    source = YouTube(youtubeLink)

    en_caption = source.captions.get_by_language_code('a.en')

    en_caption_convert_to_srt = (en_caption.generate_srt_captions())
    lineTextArray = en_caption_convert_to_srt.splitlines()
    lineTextArray = lineTextArray[2:]
    print(lineTextArray)

    desired_lines = lineTextArray[::4]
    print(desired_lines)

    # save the caption to a file named Output.txt
    text_file = open("Output.txt", "w")
    fullText = ""
    for lineText in desired_lines:
        fullText += lineText.rstrip('\n') + " "

    fullText = fullText.lower()

    text_file.write(fullText)
    text_file.close()

    # Detect fillers, get HTML red highlight
    highlightedFillers, numberOfFillers = highlightFillers("Output.txt")

    # Get HTML highlights of the other non-filler keywords
    colorTextHTML, numberOfKeywordsPerClassDictionary = getColoredHTMLText(highlightedFillers, "Output.txt")

    colorTextHTML = "<p>" + colorTextHTML + "</p>"
    colorTextHTML=colorTextHTML.replace("XYZThisMakesSureHighlightingIsDoneCorrectlyXYZ","")

    return colorTextHTML

def countNumberOfKeywordsPerClass(colorTextHTML):
    myClasses=["familiarExercisePhrases",
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
               "unfamiliarExercisePhrase"]

    numberOfKeywordsPerClassDictionary={}

    for myClass in myClasses:
        numberOfKeywordsPerClassDictionary[myClass]=colorTextHTML.count('class="'+myClass+'"')

    return numberOfKeywordsPerClassDictionary

colorTextHTML=""
transcriptText=st.empty()

# /////////////////////////////
# Runs text analysis when new youtube link is entered

if youtubeLink:
    colorTextHTML=getColorTextHTML(youtubeLink)
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

    numberOfKeywordsPerClassDictionary=countNumberOfKeywordsPerClass(colorTextHTML)

    # Update the checkbox itself
    familiarExercisePhrases = placeholder1.checkbox(
        "Familiar Exercise Phrases (" + str(numberOfKeywordsPerClassDictionary["familiarExercisePhrases"])+")")
    bodyParts = placeholder2.checkbox("Body Parts (" + str(numberOfKeywordsPerClassDictionary["bodyParts"])+")")
    directionToMove = placeholder3.checkbox(
        "Direction to Move (" + str(numberOfKeywordsPerClassDictionary["directionToMove"])+")")
    expectedBodySensation = placeholder4.checkbox(
        "Expected Body Sensation (" + str(numberOfKeywordsPerClassDictionary["expectedBodySensation"])+")")
    equipment = placeholder5.checkbox("Equipment (" + str(numberOfKeywordsPerClassDictionary["equipment"])+")")

    startingAnExercise = placeholder6.checkbox(
        "Starting an Exercise (" + str(numberOfKeywordsPerClassDictionary["startingAnExercise"]) + ")")
    stoppingAnExercise = placeholder7.checkbox("Stopping an Exercise (" + str(numberOfKeywordsPerClassDictionary["stoppingAnExercise"]) + ")")
    duration = placeholder8.checkbox(
        "Duration (" + str(numberOfKeywordsPerClassDictionary["duration"]) + ")")
    pacing = placeholder9.checkbox(
        "Pacing (" + str(numberOfKeywordsPerClassDictionary["pacing"]) + ")")
    quantityOfAnExercise = placeholder10.checkbox("Quantity of an Exercise (" + str(numberOfKeywordsPerClassDictionary["quantityOfAnExercise"]) + ")")
    transitioning = placeholder11.checkbox(
        "Transitioning (" + str(numberOfKeywordsPerClassDictionary["transitioning"]) + ")")

    brPhrase = placeholder12.checkbox(
        "Breathing (" + str(numberOfKeywordsPerClassDictionary["brPhrase"]) + ")")
    encouragingPhrases = placeholder13.checkbox(
        "Encouraging Phrases (" + str(numberOfKeywordsPerClassDictionary["encouragingPhrases"]) + ")")
    inaccessibleLocations = placeholder14.checkbox(
        "Inaccessible Locations (" + str(numberOfKeywordsPerClassDictionary["inaccessibleLocations"]) + ")")
    filler = placeholder15.checkbox(
        "Filler (" + str(numberOfKeywordsPerClassDictionary["filler"]) + ")")
    subjectivePhrases = placeholder16.checkbox(
        "Subjective Phrases (" + str(numberOfKeywordsPerClassDictionary["subjectivePhrases"]) + ")")
    unfamiliarExercisePhrase = placeholder17.checkbox(
        "Unfamiliar Exercise Phrases (" + str(numberOfKeywordsPerClassDictionary["unfamiliarExercisePhrase"]) + ")")

lightYellow = "#ffeb91"
lightGreen = "#a1e3aa"
lightRed = "#f0986c"

# /////////////////////////////
# Changes the highlight colors when checkboxes are pressed
# Table 1

if familiarExercisePhrases:
    colorTextHTML=colorTextHTML.replace('<span style="background-color:#ffffff" class="familiarExercisePhrases">',
                          '<span style="background-color:'+str(lightYellow)+'" class="familiarExercisePhrases">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if bodyParts:
    colorTextHTML=colorTextHTML.replace('<span style="background-color:#ffffff" class="bodyParts">',
                          '<span style="background-color:'+str(lightYellow)+'" class="bodyParts">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if directionToMove:
    colorTextHTML=colorTextHTML.replace('<span style="background-color:#ffffff" class="directionToMove">',
                          '<span style="background-color:'+str(lightYellow)+'" class="directionToMove">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if expectedBodySensation:
    colorTextHTML=colorTextHTML.replace('<span style="background-color:#ffffff" class="expectedBodySensation">',
                          '<span style="background-color:'+str(lightYellow)+'" class="expectedBodySensation">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if equipment:
    colorTextHTML=colorTextHTML.replace('<span style="background-color:#ffffff" class="equipment">',
                          '<span style="background-color:'+str(lightYellow)+'" class="equipment">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

# /////////////////////////////
# Table 2

if startingAnExercise:
    colorTextHTML=colorTextHTML.replace('<span style="background-color:#ffffff" class="startingAnExercise">',
                          '<span style="background-color:'+str(lightGreen)+'" class="startingAnExercise">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if stoppingAnExercise:
    colorTextHTML=colorTextHTML.replace('<span style="background-color:#ffffff" class="stoppingAnExercise">',
                          '<span style="background-color:'+str(lightGreen)+'" class="stoppingAnExercise">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if duration:
    colorTextHTML=colorTextHTML.replace('<span style="background-color:#ffffff" class="duration">',
                          '<span style="background-color:'+str(lightGreen)+'" class="duration">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if pacing:
    colorTextHTML=colorTextHTML.replace('<span style="background-color:#ffffff" class="pacing">',
                          '<span style="background-color:'+str(lightGreen)+'" class="pacing">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if quantityOfAnExercise:
    colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="quantityOfAnExercise">',
                                          '<span style="background-color:'+str(lightGreen)+'" class="quantityOfAnExercise">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if transitioning:
    colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="transitioning">',
                                          '<span style="background-color:'+str(lightGreen)+'" class="transitioning">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

# /////////////////////////////
# Table 3

if brPhrase:
    colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="brPhrase">',
                                          '<span style="background-color:'+str(lightRed)+'" class="brPhrase">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if encouragingPhrases:
    colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="encouragingPhrases">',
                                          '<span style="background-color:'+str(lightRed)+'" class="encouragingPhrases">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if inaccessibleLocations:
    colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="inaccessibleLocations">',
                                          '<span style="background-color:'+str(lightRed)+'" class="inaccessibleLocations">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if filler:
    colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="filler">',
                                          '<span style="background-color:'+str(lightRed)+'" class="filler">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if subjectivePhrases:
    colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="subjectivePhrases">',
                                          '<span style="background-color:'+str(lightRed)+'" class="subjectivePhrases">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

if unfamiliarExercisePhrase:
    colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="unfamiliarExercisePhrase">',
                                          '<span style="background-color:'+str(lightRed)+'" class="unfamiliarExercisePhrase">')
    transcriptText.empty()
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)