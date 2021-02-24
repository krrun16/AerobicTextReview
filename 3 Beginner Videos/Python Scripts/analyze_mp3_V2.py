import pandas as pd
import numpy as np

#V2 of labels 
#Video 1
#Youtube length in seconds is 1,087
vid_one_V2_data=pd.read_csv("Labels_Video_#1_V2.txt",
           delim_whitespace=True,
           skipinitialspace=True)
vid_one_V2_data1 = vid_one_V2_data.drop(columns=["LABEL"])
vid_one_V2_data2 = vid_one_V2_data1.assign(length = vid_one_V2_data["STOP"] - 
                                                vid_one_V2_data["START"])
vid_one_V2_total_voc = vid_one_V2_data2.sum(axis=0)
vid_one_V2_total_voc = vid_one_V2_total_voc["length"]
vid_one_V2_total_voc


#Video 2
#Youtube length in seconds is 2,370
vid_two_V2_data=pd.read_csv("Labels_Video_#2_V2.txt",
           delim_whitespace=True,
           skipinitialspace=True)
vid_two_V2_data.tail()
vid_two_V2_data1 = vid_two_V2_data.drop(columns=["LABEL"])
vid_two_V2_data2 = vid_two_V2_data1.assign(length = vid_two_V2_data["STOP"] - 
                                                vid_two_V2_data["START"])
vid_two_V2_total_voc = vid_two_V2_data2.sum(axis=0)
vid_two_V2_total_voc = vid_two_V2_total_voc["length"]
vid_two_V2_total_voc


#Video 3
#Youtube length in seconds is 1,751
vid_three_V2_data=pd.read_csv("Labels_Video_#3_V2.txt",
           delim_whitespace=True,
           skipinitialspace=True)
vid_three_V2_data.tail()
vid_three_V2_data1 = vid_three_V2_data.drop(columns=["LABEL"])
vid_three_V2_data2 = vid_three_V2_data1.assign(length = vid_three_V2_data["STOP"] - 
                                                vid_three_V2_data["START"])
vid_three_V2_total_voc = vid_three_V2_data2.sum(axis=0)
vid_three_V2_total_voc = vid_three_V2_total_voc["length"]
vid_three_V2_total_voc

#First go: 640.43 seconds of instruction
#V2:       716.82 seconds of instruction 