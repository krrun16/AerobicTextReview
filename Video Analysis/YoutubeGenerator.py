from youtubesearchpython import VideosSearch
import json

numVideos = 10
videosSearch = VideosSearch("beginner workout", limit = numVideos)

# jsonStr = json.dumps(videosSearch.result(), indent = 4, sort_keys=True)
# print(jsonStr)

jsonObj = videosSearch.result()
for i in range(0, numVideos):
    print(jsonObj["result"][i]["title"] + ", " + jsonObj["result"][i]["link"])
    print("\n")