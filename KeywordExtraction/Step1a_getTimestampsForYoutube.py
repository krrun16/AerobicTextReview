# Python 3.7 (There could be bugs with other versions like 3.8)
# pip install streamlit
# pip install pytube3==10.8.5
# pip install youtube_dl
# pip install deepsegment
# pip install tensorflow==1.14
# pip install keras==2.2.5
# pip install nltk

import youtube_dl
import os
import subprocess

fullTexts=[]
audioFiles=[]

def getTimestampsJsonFromYoutubeLink(youtubeLink):
    myFilename=os.getcwd()+"/gentle/YoutubeOutput.mp3"

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

    os.chdir('gentle')

    query = subprocess.Popen("python3 align.py YoutubeOutput.mp3 YoutubeOutput.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = query.communicate()

    print("Yay output!")
    print(output)

    return output
    # timestampsJson=run(["python3", "align.py","YoutubeOutput.mp3","YoutubeOutput.txt"]).stdout
    # return timestampsJson

import json
import xlsxwriter

def turnTimestampsJsonFileIntoCSV(jsonFilename):
    with open(jsonFilename, "r") as myfile:
        stringData = json.load(myfile)

    print("More string data yay")
    print(stringData)

    workbook = xlsxwriter.Workbook("YoutubeOutput_timestamps_fromFile.xlsx")
    worksheet = workbook.add_worksheet()

    words=stringData["words"][0]
    print("More words yay")
    print(words)

    i=0
    for word in words:
        worksheet.write_row(i, 0, [word["alignedWord"],word["alignedWord"],word["start"],word["end"]])
        i+=1

    workbook.close()

import csv

def turnTimestampsJsonIntoCSV(jsonText):
    with open('YoutubeOutput_timestamps.csv', mode='w') as csv_file:
        myWriter = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        jsonData=json.loads(jsonText)

        words=jsonData["words"]
        print("Yay words")
        print(words)

        for word in words:
            print(word)
            if 'alignedWord' in word:
                myWriter.writerow([word['alignedWord'],word['alignedWord'],word['start'],word['end']])
            else:
                myWriter.writerow([word['word'],word['word'],"",""])

