import pandas as pd
import sys

#Manually fixed/placed labels

#Video 
#"C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Videos/Video_3/Edited_labels_vocals.txt"

#Reads the input file if using command line
filename = sys.argv[1]

#Creates the dataframe off of the audio file
vid_data=pd.read_csv(filename, header=None, delim_whitespace=True)

#Using the ending of the last label to depict video length
TIME = vid_data.iloc[-1, 1]

#Dropping the label column then calculating duration of label.
vid_data1 = vid_data.drop(columns=[2])
vid_data2 = vid_data1.assign(length = vid_data[1] - 
                                                vid_data[0])

#Summing the column of instruction durations for total time speaking
vid_total_voc = vid_data2.sum(axis=0)
vid_total_voc = vid_total_voc["length"]
vid_total_voc

#Dividing time of instructing over total time of video to find percent of instruction
percent_of_instruction = (vid_total_voc / TIME) * 100.0
print(percent_of_instruction)