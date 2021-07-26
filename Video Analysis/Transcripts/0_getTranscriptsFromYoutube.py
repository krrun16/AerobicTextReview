# STUFF TO INSTALL:
# pip install tensorflow==1.14
# pip install keras==2.2.5
# pip install youtube-transcript-api
# pip install deepsegment

import urllib.parse
from youtube_transcript_api import YouTubeTranscriptApi

youtubeLinks=[["https://www.youtube.com/watch?v=WIHy-ZnSndA","Video_TestFile.txt"]]

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

    fullText = fullText.lower()
    file1 = open(youtubeLink[1], "w")
    file1.write(fullText)
    file1.close()
