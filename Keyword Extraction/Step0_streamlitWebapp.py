# Stuff to install:
# pip install streamlit
# pip install scikit-learn
# pip install matplotlib
# Pip install pytube3

# Run this in terminal to start the app on your computer: streamlit run Step0_streamlitWebapp.py

# /////////////////////////////
import streamlit as st
st.title("Exercise Transcript Analysis")
st.write("Identifies 17 different classes of exercise transcript phrases")

# /////////////////////////////
# Different checkbox options
st.sidebar.write("Select Classes:")
st.sidebar.markdown("__Table 1 (specify body movements):__")
familiarExercisePhrases = st.sidebar.checkbox("Familiar Exercise Phrases")
bodyParts = st.sidebar.checkbox("Body Parts")
directionToMove = st.sidebar.checkbox("Direction to Move")
expectedBodySensation = st.sidebar.checkbox("Expected Body Sensation")
equipment = st.sidebar.checkbox("Equipment")
st.sidebar.markdown("____")

st.sidebar.markdown("__Table 2 (specify timing):__")
startingAnExercise = st.sidebar.checkbox("Starting an Exercise")
stoppingAnExercise = st.sidebar.checkbox("Stopping an Exercise")
duration = st.sidebar.checkbox("Duration")
pacing = st.sidebar.checkbox("Pacing")
quantityOfAnExercise = st.sidebar.checkbox("Quantity of an Exercise")
transitioning = st.sidebar.checkbox("Transitioning")
st.sidebar.markdown("____")

st.sidebar.markdown("__Table 3 (does not specify movements or time):__")
breathing = st.sidebar.checkbox("Breathing")
encouragingPhrases = st.sidebar.checkbox("Encouraging Phrases")
inaccessibleLocations = st.sidebar.checkbox("Inaccessible Locations")
filler = st.sidebar.checkbox("Filler")
subjectivePhrases = st.sidebar.checkbox("Subjective Phrases")
unfamiliarExercisePhrase = st.sidebar.checkbox("Unfamiliar Exercise Phrase")

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
    highlightedFillers = highlightFillers("Output.txt")

    # Get HTML highlights of the other non-filler keywords
    colorTextHTML = getColoredHTMLText(highlightedFillers, "Output.txt")
    colorTextHTML = "<p>" + colorTextHTML + "</p>"

    return colorTextHTML

colorTextHTML=""
transcriptText=st.empty()

# /////////////////////////////
# Runs text analysis when new youtube link is entered

if youtubeLink:
    colorTextHTML=getColorTextHTML(youtubeLink)
    transcriptText.markdown(colorTextHTML, unsafe_allow_html=True)

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

if breathing:
    colorTextHTML = colorTextHTML.replace('<span style="background-color:#ffffff" class="breathing">',
                                          '<span style="background-color:'+str(lightRed)+'" class="breathing">')
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