import pandas as pd
import numpy as np

#V2 of labels 

vid_one_V2_data=pd.read_csv("Labels_Video_#1_V2.txt",
           delim_whitespace=True,
           skipinitialspace=True)
vid_one_V2_data.tail()
vid_one_V2_data1 = vid_one_V2_data.drop(columns=["LABEL"])
vid_one_V2_data2 = vid_one_V2_data1.assign(length = vid_one_V2_data["STOP"] - 
                                                vid_one_V2_data["START"])
vid_one_V2_total_voc = vid_one_V2_data2.sum(axis=0)
vid_one_V2_total_voc = vid_one_V2_total_voc["length"]
vid_one_V2_total_voc

#Isn't the legit length of the video but rather from first vocal to last
#Youtube length in seconds is 1,087
#How many seconds was the delay from me hittingr ecord to me hittingn
#Play on Youtube
vid_one_data2
STOP = len(vid_one_V2_data2)
vid_one_length = vid_one_data2.STOP[STOP] - vid_one_data2.START[1]

vid_one_instruct_percent = vid_one_total_voc / vid_one_length
vid_one_instruct_percent