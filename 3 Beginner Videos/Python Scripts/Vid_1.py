import pandas as pd
import numpy as np

#Manually fixed/placed labels


#Video 1
vid_one_V2_data=pd.read_csv("3 Beginner Videos\Labels\Labels_Video_#1_V2.txt",
           delim_whitespace=True,
           skipinitialspace=True)

vid_one_V2_data

vid_one_V2_data1 = vid_one_V2_data.drop(columns=["LABEL"])
vid_one_V2_data2 = vid_one_V2_data1.assign(length = vid_one_V2_data["STOP"] - 
                                                vid_one_V2_data["START"])
vid_one_V2_total_voc = vid_one_V2_data2.sum(axis=0)
vid_one_V2_total_voc = vid_one_V2_total_voc["length"]
vid_one_V2_total_voc

vid_one_V3_data_wo_deletions=pd.read_csv("3 Beginner Videos\Labels\Labels_Video_#1_V3.txt",
           delim_whitespace=True,
           skipinitialspace=True)

deletions_vid_1 = [50, 205, 261, 274, 333 , 624, 625]
 
vid_one_V3_data = vid_one_V3_data_wo_deletions[~vid_one_V3_data_wo_deletions.LABEL.isin(deletions_vid_1)]

vid_one_V3_data1 = vid_one_V3_data.drop(columns=["LABEL"])
vid_one_V3_data2 = vid_one_V3_data1.assign(length = vid_one_V3_data["STOP"] - 
                                                vid_one_V3_data["START"])
vid_one_V3_total_voc = vid_one_V3_data2.sum(axis=0)
vid_one_V3_total_voc = vid_one_V3_total_voc["length"]
vid_one_V3_total_voc

#First go:  648.63 seconds of instruction 
#V2:        649.31 seconds of instruction
#Time of video is 1056 seconds

#Vid_3 Cohen's Kappa

BL = len(deletions_vid_1)
TR = (len(vid_one_V3_data_wo_deletions)) - len(vid_one_V2_data)
TL = len(vid_one_V3_data) - TR
BR = TL - 1


P_O = (TL + BR) / (TL + TR + BL + BR)

p_yes_at_random = (TL + TR) / (TL + TR + BR + BL) * (TL + BL) / (TL + TR + BR + BL)

p_no_at_random = (BL + BR) / (TL + TR + BR + BL) * (TR + BR) / (TL + TR + BR + BL)

P_E = p_yes_at_random + p_no_at_random

Kappa = (P_O - P_E) / (1 - P_E)
Kappa

TL
TR
BL
BR