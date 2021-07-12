from Step0_highlightFillers import *
from Step1_highlightSearchableKeywords import *

# Pip install pytube3
from pytube import YouTube

source = YouTube('https://www.youtube.com/watch?v=gC_L9qAHVJ8 ')

en_caption = source.captions.get_by_language_code('a.en')

en_caption_convert_to_srt =(en_caption.generate_srt_captions())
lineTextArray = en_caption_convert_to_srt.splitlines()
lineTextArray=lineTextArray[2:]
print(lineTextArray)

desired_lines = lineTextArray[::4]
print(desired_lines)

#save the caption to a file named Output.txt
text_file = open("Output.txt", "w")
fullText=""
for lineText in desired_lines:
    fullText += lineText.rstrip('\n') + " "

fullText = fullText.lower()

text_file.write(fullText)
text_file.close()

# Detect fillers, get HTML red highlight
highlightedFillers = highlightFillers("Output.txt")

# Get HTML highlights of the other non-filler keywords
colorTextHTML = getColoredHTMLText(highlightedFillers,"Output.txt")

print(colorTextHTML)
print()