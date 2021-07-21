# STUFF TO INSTALL:
# pip install tensorflow==1.14
# pip install keras==2.2.5
# pip install pytube==10.8.5
# pip install deepsegment

from pytube import YouTube

youtubeLinks=[["https://www.youtube.com/watch?v=WIHy-ZnSndA","Video_TestHasfit.txt"]
]

for youtubeLink in youtubeLinks:
    source = YouTube(youtubeLink[0])

    try:
        en_caption = source.captions['en']
    except:
        en_caption = source.captions['a.en']

    # en_caption = source.captions.get_by_language_code('a.en')

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
    file1 = open(youtubeLink[1], "w")
    file1.write(fullText)
    file1.close()