import youtube_dl
import os
import subprocess

myFilename=os.getcwd()+"/Video 10 Bodybuilder.mp3"
youtubeLink="https://www.youtube.com/watch?v=YdB1HMCldJY"

if os.path.isfile(myFilename):
    os.remove(myFilename)

ydl_opts = {
    'outtmpl': myFilename,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([youtubeLink])