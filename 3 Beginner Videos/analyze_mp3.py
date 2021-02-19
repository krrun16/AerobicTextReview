import pandas as pd
import numpy as np

#First calculation with assumption of less accurate labels

vid_one_data=pd.read_csv("Labels Video #1.txt",
           delim_whitespace=True,
           skipinitialspace=True)
vid_one_data.tail()
vid_one_data1 = vid_one_data.drop(columns=["LABEL"])
vid_one_data2 = vid_one_data1.assign(length = vid_one_data["STOP"] - 
                                                vid_one_data["START"])
vid_one_total_voc = vid_one_data2.sum(axis=0)
vid_one_total_voc = vid_one_total_voc["length"]
vid_one_total_voc

#Isn't the legit length of the video but rather from first vocal to last
#Youtube length in seconds is 1,087
#How many seconds was the delay from me hittingr ecord to me hittingn
#Play on Youtube
vid_one_data2
vid_one_length = vid_one_data2.STOP[1503] - vid_one_data2.START[1]

vid_one_instruct_percent = vid_one_total_voc / vid_one_length
vid_one_instruct_percent


vid_two_data=pd.read_csv("Labels Video #2.txt",
           delim_whitespace=True,
           skipinitialspace=True)
vid_two_data.head()
vid_two_data1 = vid_two_data.drop(columns=["LABEL"])
vid_two_data2 = vid_two_data1.assign(length = vid_two_data["STOP"] - 
                                                vid_two_data["START"])                                      
vid_two_total_voc = vid_two_data2.sum(axis=0)
vid_two_total_voc = vid_two_total_voc["length"]

#Switch tracks of audio on Audacity at 1,058
#Isn't the legit length of the video but rather from first vocal to last
#Youtube length in seconds is 1,800
#How many seconds was the delay from me hittingr ecord to me hittingn
#Play on Youtube
vid_two_data2
vid_two_length = vid_two_data2.STOP[2277] - vid_two_data2.START[1]

vid_two_instruct_percent = vid_two_total_voc / vid_two_length
vid_two_instruct_percent


vid_three_data=pd.read_csv("Labels Video #3.txt",
           delim_whitespace=True,
           skipinitialspace=True)
vid_three_data.head()
vid_three_data1 = vid_three_data.drop(columns=["LABEL"])
vid_three_data2 = vid_three_data1.assign(length = vid_three_data["STOP"] - 
                                                vid_three_data["START"])                                      
vid_three_total_voc = vid_three_data2.sum(axis=0)
vid_three_total_voc = vid_three_total_voc["length"]
vid_three_total_voc

#Isn't the legit length of the video but rather from first vocal to last
#Youtube length in seconds is 1,751
#How many seconds was the delay from me hittingr ecord to me hittingn
#Play on Youtube
vid_three_data2
vid_three_length = vid_three_data2.STOP[2339] - vid_three_data2.START[1]

vid_three_instruct_percent = vid_three_total_voc / vid_three_length
vid_three_instruct_percent

print(v)