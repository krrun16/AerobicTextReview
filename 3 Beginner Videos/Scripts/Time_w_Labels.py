import pandas as pd
import sys

#Manually fixed/placed labels

#Video 

filename = sys.argv[1]

vid_data=pd.read_csv(filename, header=None, delim_whitespace=True)

TIME = vid_data.iloc[-1, 1]

vid_data1 = vid_data.drop(columns=[2])
vid_data2 = vid_data1.assign(length = vid_data[1] - 
                                                vid_data[0])
vid_total_voc = vid_data2.sum(axis=0)
vid_total_voc = vid_total_voc["length"]
vid_total_voc

percent_of_instruction = (vid_total_voc / TIME) * 100.0
print(percent_of_instruction)