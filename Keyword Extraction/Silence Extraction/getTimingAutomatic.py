from __future__ import unicode_literals

# Install the following:
# cd into the "gentle" folder and then type: ./install.sh

# pip install --upgrade incremental
#  pip install Twisted==16.4.1
# pip install youtube_dl

# For Macs:
# brew install ffmpeg

# https://github.com/lowerquality/gentle
# https://github.com/lowerquality/gentle/issues/128

from pytube import YouTube
import youtube_dl
import os
import requests
from subprocess import call

youtubeLinks=[
              ["https://www.youtube.com/watch?v=ZVhlXEYb31o",7],
              ["https://www.youtube.com/watch?v=qWy_aOlB45Y",8]]

for youtubeLink in youtubeLinks:
    myFilename=os.getcwd()+"/Video "+str(youtubeLink[1])+".wav"
    ydl_opts = {
        'outtmpl': myFilename,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtubeLink[0]])

    source = YouTube(youtubeLink[0])

    try:
        en_caption = en_caption = source.captions['en']
    except:
        en_caption = en_caption = source.captions['a.en']

    en_caption_convert_to_srt = (en_caption.generate_srt_captions())
    lineTextArray = en_caption_convert_to_srt.splitlines()
    lineTextArray = lineTextArray[2:]
    print(lineTextArray)

    desired_lines = lineTextArray[::4]
    print(desired_lines)

    # save the caption to a file named Output.txt
    text_file = open("Video "+str(youtubeLink[1])+".txt", "w")
    fullText = ""
    for lineText in desired_lines:
        fullText += lineText.rstrip('\n') + " "

    fullText = fullText.lower()

    text_file.write(fullText)
    text_file.close()

# python3 align.py "Output.mp3" "Output.txt"
# os.chdir(os.getcwd()+"/gentle")
#
# call(["python3","align.py", "Output.mp3","Output.txt"])

# curl -F "audio=$Output.mp3" -F "transcript=$Output.txt" "http://localhost:8765/transcriptions?async=false"