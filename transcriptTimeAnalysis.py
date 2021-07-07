import csv
import pandas as pd

numVideos = 7

# Get rid of 2nd column in all files
for x in range(numVideos):
    filename = "Video Analysis/Transcripts/video_" + str(x+1) + "_TimeStamps.csv"
    data = pd.read_csv(filename)
    data.pop("GENTLE_GENERATED")
    data.to_csv("Video Analysis/Transcripts/video_" + str(x+1) + "_TimeStampsClean.csv", index=False)

# Goes through rows to find silences
for x in range(numVideos):
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

# Going through the rows and connecting words into phrases based on silences
for x in range(numVideos):
    filename = "Video Analysis/Transcripts/video_" + str(x + 1) + "_TimeStampsClean.csv"
    data = pd.read_csv(filename)
    with open("Video Analysis/Transcripts/video_" + str(x + 1) + "_SplitPhrasesByTime.csv", 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["PHRASE","START","END"])

        totalRows = len(data.index)
        currentPhrase = ""
        currentStart = 0
        for n in range(totalRows-1):
            firstEnd = float(data.iloc[n]["END_TIME"])
            secondStart = float(data.iloc[n + 1]["START_TIME"])
            phrase = data.iloc[n]["ORIGINAL_WORD"]
            if currentPhrase == "":
                currentStart = float(data.iloc[n]["START_TIME"])
            if firstEnd == "" or secondStart == "":
                phrase += currentPhrase
                continue
            silenceLength = secondStart - firstEnd
            if silenceLength >= 0.2: # breaks between phrases are assumed to be 0.2 seconds (0.5 was too big)
                currentPhrase += phrase
                writer.writerow([currentPhrase,str(currentStart),str(firstEnd)])
                currentPhrase = ""
            else:
                currentPhrase += phrase + " "