import pandas as pd
#import numpy as np

#Manually fixed/placed labels

#Video 3
vid_three_V2_data=pd.read_csv(r"C:\Users\calvi\OneDrive - University of Iowa\Documents\aerobictextreview\3 Beginner Videos\Calvin_Videos\Video 3\labels_8.txt", delim_whitespace=True)

vid_three_V2_data1 = vid_three_V2_data.drop(columns=["LABEL"])
vid_three_V2_data2 = vid_three_V2_data1.assign(length = vid_three_V2_data["STOP"] - vid_three_V2_data["START"])
vid_three_V2_total_voc = vid_three_V2_data2.sum(axis=0)
vid_three_V2_total_voc = vid_three_V2_total_voc["length"]

percent_of_instruction = (vid_three_V2_total_voc / 1703) * 100.0


#vid_three_V3_data_wo_deletions=pd.read_csv("3 Beginner Videos\Labels\Labels_Video_#3_V3.txt",
 #          delim_whitespace=True,
  #         skipinitialspace=True)

#deletions_vid_3 = [74, 75, 154, 166, 168, 172, 173, 199, 215, 216, 278, 281, 
 #           283, 304, 319, 324, 325, 326, 330, 332, 334, 338, 345, 347, 
  #          350, 351, 353, 354, 356, 359, 386, 408, 411, 419, 420, 429, 
   #         458, 468, 473, 480, 513, 514, 515, 520, 521, 571, 581, 585, 
    #        600, 627, 633, 638, 644, 666, 667, 668, 671, 672, 673, 681, 
     #       683, 684, 685, 686, 687, 688, 695, 695, 710, 711, 714, 733, 
      #      737, 740, 745, 747, 752, 753, 761, 764, 767, 768, 769, 770, 
       #     771, 772, 774, 783, 787, 791, 794, 797, 799, 815, 821, 827, 
        #    885, 886, 890, 897, 898, 900, 902, 903, 907, 909, 912, 915, 
         #   926, 956, 962, 963, 965, 968, 969, 970, 971, 972, 975, 976, 
          #  977, 978, 979, 980, 989, 991, 998, 999, 1036, 1037, 1051, 
          #  1057, 1058, 1079, 1096, 1100, 1131, 1133, 1134, 1135, 1146, 
          #  1149, 1166, 1167, 1173, 1174, 1175, 1176, 1178, 1184, 1185, 
          #  1186, 1212, 1213, 1214, 1216, 1217, 1220, 1221, 1222, 1261, 
          #  1359, 1363, 1364, 1365, 1369]


#vid_three_V3_data = vid_three_V3_data_wo_deletions[~vid_three_V3_data_wo_deletions.LABEL.isin(deletions_vid_3)]

#vid_three_V3_data1 = vid_three_V3_data.drop(columns=["LABEL"])
#vid_three_V3_data2 = vid_three_V3_data1.assign(length = vid_three_V3_data["STOP"] - 
                                       #         vid_three_V3_data["START"])
#vid_three_V3_total_voc = vid_three_V3_data2.sum(axis=0)
#vid_three_V3_total_voc = vid_three_V3_total_voc["length"]
#vid_three_V3_total_voc

#First go: 716.82 seconds of instruction 
#V2:       720.65 seconds of instruction
#Time of Video is 1,751 seconds

#Vid_3 Cohen's Kappa

#BL = len(deletions_vid_3)
#TR = (len(vid_three_V3_data_wo_deletions)) - len(vid_three_V2_data)
#TL = len(vid_three_V3_data) - TR
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