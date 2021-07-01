import csv
import pandas as pd

# Get rid of 2nd column in all files
for x in range(6):
    filename = "Video Analysis/Transcripts/video_" + str(x+1) + "_TimeStamps.csv"
    data = pd.read_csv(filename)
    data.pop("GENTLE_GENERATED")
    data.to_csv("Video Analysis/Transcripts/video_" + str(x+1) + "_TimeStampsClean.csv", index=False)

# Goes through rows to find silences
for x in range(6):
    filename = "Video Analysis/Transcripts/video_" + str(x + 1) + "_TimeStampsClean.csv"
    data = pd.read_csv(filename)
    with open("Video Analysis/Transcripts/video_" + str(x + 1) + "_Silences.csv", 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["START","END","LENGTH"])

        totalRows = len(data.index)
        for n in range(totalRows-1):
            firstEnd = float(data.iloc[n]["END_TIME"])
            secondStart = float(data.iloc[n + 1]["START_TIME"])
            if firstEnd == "" or secondStart == "":
                continue
            silenceLength = secondStart - firstEnd
            if silenceLength >= 4: # detects silences longer than 4 seconds
                writer.writerow([str(firstEnd),str(secondStart),str(silenceLength)])
