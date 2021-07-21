# STUFF TO INSTALL:
# pip install tensorflow==1.14
# pip install keras==2.2.5
# pip install pytube==10.8.5
# pip install deepsegment

from pytube import YouTube
from deepsegment import DeepSegment

youtubeLinks=[["https://www.youtube.com/watch?v=WIHy-ZnSndA","HasFit"],
["https://www.youtube.com/watch?v=gC_L9qAHVJ8","Body Project"],
["https://www.youtube.com/watch?v=JkVHrA5o23o","MadFit"],
["https://www.youtube.com/watch?v=CPI_Ve7vsHs","Chloe Ting"],
["https://www.youtube.com/watch?v=OyLiIrA46SY","BeFit"]
]

segmenter = DeepSegment('en')
mySentences=[]

for youtubeLink in youtubeLinks:
    source = YouTube(youtubeLink[0])

    en_caption = source.captions.get_by_language_code('a.en')

    en_caption_convert_to_srt = (en_caption.generate_srt_captions())
    lineTextArray = en_caption_convert_to_srt.splitlines()
    lineTextArray = lineTextArray[2:]
    print(lineTextArray)

    desired_lines = lineTextArray[::4]
    print(desired_lines)

    fullText = ""
    for lineText in desired_lines:
        fullText += lineText.rstrip('\n') + " "

    fullText = fullText.lower()

    thisVideoSentencesArray = segmenter.segment_long(fullText)

    for sentence in thisVideoSentencesArray:
        mySentences.append([sentence, youtubeLink[1]])

import csv
import os

with open(os.getcwd()+"/Sentences_Vids123456_longerFillerDataset.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    for mySentence in mySentences:
        writer.writerow([mySentence[0], mySentence[1]])
