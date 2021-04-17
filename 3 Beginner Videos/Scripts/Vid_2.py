import pandas as pd
#import numpy as np

#Manually fixed/placed labels


#Video 2
vid_two_V2_data=pd.read_csv(r"C:\Users\calvi\OneDrive - University of Iowa\Documents\aerobictextreview\3 Beginner Videos\Calvin_Videos\Video 2\labels_8.txt", delim_whitespace=True)

vid_two_V2_data

vid_two_V2_data1 = vid_two_V2_data.drop(columns=["LABEL"])
vid_two_V2_data2 = vid_two_V2_data1.assign(length = vid_two_V2_data["STOP"] - 
                                                vid_two_V2_data["START"])
vid_two_V2_total_voc = vid_two_V2_data2.sum(axis=0)
vid_two_V2_total_voc = vid_two_V2_total_voc["length"]
vid_two_V2_total_voc

percent_of_instruction = (vid_two_V2_total_voc / 2328) * 100.0

#vid_two_V3_data_wo_deletions=pd.read_csv("3 Beginner Videos\Labels\Labels_Video_#2_V3.txt",
 #          delim_whitespace=True,
  #         skipinitialspace=True)

#vid_two_V3_data_wo_deletions

#deletions_vid_2 = [1, 44, 43, 45, 58, 78, 95, 100, 102, 103, 120, 121, 
 #                   150, 151, 169, 170, 177, 193, 213, 214, 216, 217, 
  #                  219, 232, 249, 254, 261, 262, 263, 266, 276, 279, 
   #                 280, 281, 283, 285, 289, 290, 300, 302, 306, 307, 
    #                310, 314, 325, 326, 337, 338, 345, 362, 367, 381, 
     #               383, 391, 392, 393, 395, 400, 408, 422, 428, 468, 
      #              479, 487, 498, 499, 500, 518, 519, 526, 536, 537, 
       #             542, 543, 546, 552, 559, 561, 562, 565, 570, 571, 
        #            573, 578, 579, 580, 585, 588, 589, 590, 592, 595, 
         #           597, 612, 613, 628, 632, 638, 645, 650, 652, 654, 
          #          667, 668, 679, 680, 689, 691, 692, 694, 698, 700, 
           #         703, 706, 713, 724, 730, 731, 735, 736, 738, 748, 
            #        776, 777, 780, 782, 787, 788, 797, 800, 802, 825, 
             #       833, 834, 838, 841, 847, 849, 852, 882, 885, 886, 
              #      890, 891, 893, 895, 927, 930, 936, 940, 974, 975, 
               #     978, 981, 985, 986, 987, 988, 994, 1003, 1006, 
                #    1007, 1010, 1011, 1015, 1016, 1025, 1028, 1033, 
                 #   1035, 1052, 1057, 1075, 1077, 1083, 1090, 1091, 
                  #  1098, 1119, 1148, 1153, 1163, 1165, 1187, 1191, 
                  #  1193, 1194, 1198, 1200, 1213, 1216, 1217, 1223, 
                  #  1229, 1249, 1276, 1277, 1278, 1289, 1290, 1292, 
                  #  1299, 1312, 1341, 1342, 1344, 1347, 1349, 1357, 
                  #  1358, 1362, 1372, 1375, 1386, 1387, 1396, 1397, 
                  #  1400, 1404, 1406, 1409, 1411, 1412, 1418, 1427, 
                  #  1428, 1429, 1430, 1432, 1433, 1441, 1447, 1450 , 
                  #  1459, 1460, 1462, 1465, 1466, 1474, 1477, 1488, 
                  #  1495, 1504, 1505]
 
#vid_two_V3_data = vid_two_V3_data_wo_deletions[~vid_two_V3_data_wo_deletions.LABEL.isin(deletions_vid_2)]

#vid_two_V3_data1 = vid_two_V3_data.drop(columns=["LABEL"])
#vid_two_V3_data2 = vid_two_V3_data1.assign(length = vid_two_V3_data["STOP"] - 
                     #                           vid_two_V3_data["START"])
#vid_two_V3_total_voc = vid_two_V3_data2.sum(axis=0)
#vid_two_V3_total_voc = vid_two_V3_total_voc["length"]
#vid_two_V3_total_voc

#First go:  1555.13 seconds of instruction 
#V2:        1562.53 seconds of instruction
#Time of video is 2,307 seconds

#Vid_2 Cohen's Kappa

#BL = len(deletions_vid_2)
#TR = (len(vid_two_V3_data_wo_deletions)) - len(vid_two_V2_data)
#TL = len(vid_two_V3_data) - TR
#BR = TL - 1

# Correct

#P_O = (TL + BR) / (TL + TR + BL + BR)

#p_yes_at_random = (TL + TR) / (TL + TR + BR + BL) * (TL + BL) / (TL + TR + BR + BL)

#p_no_at_random = (BL + BR) / (TL + TR + BR + BL) * (TR + BR) / (TL + TR + BR + BL)

#P_E = p_yes_at_random + p_no_at_random

#Kappa = (P_O - P_E) / (1 - P_E)
#Kappa

#TL
#TR
#BL
#BR