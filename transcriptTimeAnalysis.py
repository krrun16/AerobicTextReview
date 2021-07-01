import csv
import pandas as pd

def getInterval(row, filename):
    csvList = csvToList(filename)


# Get rid of 2nd column in all files
for x in range(6):
    filename = "Video Analysis/Transcripts/video_" + str(x+1) + "_TimeStamps.csv"
    data = pd.read_csv(filename)
    data.pop("GENTLE_GENERATED")
    data.to_csv("Video Analysis/Transcripts/video_" + str(x+1) + "_TimeStampsClean.csv", index=False)
