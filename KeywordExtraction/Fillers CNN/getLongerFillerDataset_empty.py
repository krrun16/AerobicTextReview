# STUFF TO INSTALL:
# pip install tensorflow==1.14
# pip install keras==2.2.5
# pip install youtube-transcript-api
# pip install deepsegment

youtubeLinks=[["https://www.youtube.com/watch?v=WIHy-ZnSndA","HasFit"],
["https://www.youtube.com/watch?v=gC_L9qAHVJ8","Body Project"],
["https://www.youtube.com/watch?v=JkVHrA5o23o","MadFit"],
["https://www.youtube.com/watch?v=CPI_Ve7vsHs","Chloe Ting"],
["https://www.youtube.com/watch?v=OyLiIrA46SY","BeFit"],
["https://www.youtube.com/watch?v=ZVhlXEYb31o","Orange Theory"],
["https://www.youtube.com/watch?v=qWy_aOlB45Y ","Fitness Blender"]
]

mySentences=[]

import urllib.parse
from youtube_transcript_api import YouTubeTranscriptApi
from deepsegment import DeepSegment

def extract_video_id(url):
    # Examples:
    # - http://youtu.be/numbersandletters
    # - http://www.youtube.com/watch?v=numbersandletters&feature=feedu
    # - http://www.youtube.com/embed/numbersandletters
    # - http://www.youtube.com/v/numbersandletters?version=3&amp;hl=en_US
    query = urllib.parse.urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com'}:
        if query.path == '/watch': return urllib.parse.parse_qs(query.query)['v'][0]
        if query.path[:7] == '/watch/': return query.path.split('/')[1]
        if query.path[:7] == '/embed/': return query.path.split('/')[2]
        if query.path[:3] == '/v/': return query.path.split('/')[2]
        # below is optional for playlists
        if query.path[:9] == '/playlist': return urllib.parse.parse_qs(query.query)['list'][0]
# returns None for invalid YouTube url

for youtubeLink in youtubeLinks:
    videoID = extract_video_id(youtubeLink[0])
    srt = YouTubeTranscriptApi.get_transcript(videoID)

    fullText = ""

    for i in srt:
        fullText += i["text"] + " "

    segmenter = DeepSegment('en')
    thisVideoSentencesArray = segmenter.segment_long(fullText)

    for sentence in thisVideoSentencesArray:
        mySentences.append([sentence, youtubeLink[1]])

import csv
import os

with open(os.getcwd()+"/Sentences_Vids12345678_longerFillerDataset_empty.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    for mySentence in mySentences:
        writer.writerow([mySentence[0], mySentence[1]])
