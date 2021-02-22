import pandas as pd
import numpy as np

#Manually fixed/placed labels


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
vid_three_V3_data=pd.read_csv("Labels_Video_#3_V3.txt",
           delim_whitespace=True,
           skipinitialspace=True)
vid_three_V3_data
deletions = [74, 75, 154, 166, 168, 172, 173, 199, 215, 216, 278, 281, 
            283, 304, 319, 324, 325, 326, 330, 332, 334, 338, 345, 347, 
            350, 351, 353, 354, 356, 359, 386, 408, 411, 419, 420, 429, 
            458, 468, 473, 480, 513, 514, 515, 520, 521, 571, 581, 585, 
            600, 627, 633, 638, 644, 666, 667, 668, 671, 672, 673, 681, 
            683, 684, 685, 686, 687, 688, 695, 695, 710, 711, 714, 733, 
            737, 740, 745, 747, 752, 753, 761, 764, 767, 768, 769, 770, 
            771, 772, 774, 783, 787, 791, 794, 797, 799, 815, 821, 827, 
            885, 886, 890, 897, 898, 900, 902, 903, 907, 909, 912, 915, 
            926, 956, 962, 963, 965, 968, 969, 970, 971, 972, 975, 976, 
            977, 978, 979, 980, 989, 991, 998, 999, 1036, 1037, 1051, 
            1057, 1058, 1079, 1096, 1100, 1131, 1133, 1134, 1135, 1146, 
            1149, 1166, 1167, 1173, 1174, 1175, 1176, 1178, 1184, 1185, 
            1186, 1212, 1213, 1214, 1216, 1217, 1220, 1221, 1222, 1261, 
            1359, 1363, 1364, 1365, 1369]

vid_three_V3_data 
vid_three_V3_data = vid_three_V3_data[~vid_three_V3_data.LABEL.isin(deletions)]
len(deletions)
vid_three_V3_data
vid_three_V3_data1 = vid_three_V3_data.drop(columns=["LABEL"])
vid_three_V3_data2 = vid_three_V3_data1.assign(length = vid_three_V3_data["STOP"] - 
                                                vid_three_V3_data["START"])
vid_three_V3_total_voc = vid_three_V3_data2.sum(axis=0)
vid_three_V3_total_voc = vid_three_V3_total_voc["length"]
vid_three_V3_total_voc

#First go: 640.43 seconds of instruction
#V2:       716.82 seconds of instruction 
#V3:       720.65 seconds of instrictoon