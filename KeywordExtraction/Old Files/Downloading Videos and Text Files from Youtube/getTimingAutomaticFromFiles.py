from pytube import YouTube
import youtube_dl
import os

youtubeLinks=[["https://www.youtube.com/watch?v=WIHy-ZnSndA",1],
              ["https://www.youtube.com/watch?v=gC_L9qAHVJ8",3],
              ["https://www.youtube.com/watch?v=VWj8ZxCxrYk",4],
              ["https://www.youtube.com/watch?v=CD6BCdFHogg",5],
              ["https://www.youtube.com/watch?v=OyLiIrA46SY",6],
              ["https://www.youtube.com/watch?v=ZVhlXEYb31o",7],
              ["https://www.youtube.com/watch?v=qWy_aOlB45Y",8]]

for youtubeLink in youtubeLinks:
    myFilename=os.getcwd()+"/Video "+str(youtubeLink[1])+".mp3"
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
        ydl.download([youtubeLink[0]])

    source = YouTube(youtubeLink[0])

    try:
        en_caption = source.captions['en']
    except:
        en_caption = source.captions['a.en']

    en_caption_convert_to_srt = (en_caption.generate_srt_captions())
    lineTextArray = en_caption_convert_to_srt.splitlines()
    lineTextArray = lineTextArray[2:]
    print(lineTextArray)

    desired_lines = lineTextArray[::4]
    print(desired_lines)

    # save the caption to a file named Output.txt
    text_file = open("/Video"+str(youtubeLink[1])+".txt", "w")

    fullText = ""
    for lineText in desired_lines:
        fullText += lineText.rstrip('\n') + " "

    fullText = fullText.lower()
    text_file.write(fullText)
    text_file.close()
