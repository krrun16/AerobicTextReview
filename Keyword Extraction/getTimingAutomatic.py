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



import youtube_dl
import os
from subprocess import call

myFilename=os.getcwd()+"/gentle/Output.mp3"
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
    ydl.download(['https://www.youtube.com/watch?v=WIHy-ZnSndA'])

os.chdir(os.getcwd()+"/gentle")

call(["python3","align.py", "Output.mp3","Output.txt"])
