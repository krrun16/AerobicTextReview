from scipy.io.wavfile import read
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read audio samples using frame rate and # of frames
input_data = read("C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Calvin_Videos/Video 1/vocals.wav")
input_data2 = read("C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Calvin_Videos/Video 2/vocals.wav")

# extract solely the frames clipped
audio = pd.DataFrame(input_data[1])


#Delete the second repetitive column
audio2 = audio.drop(columns=[1])

#Delete zero values
audio3 = audio2[audio2 != 0]

#Change negative values to positive inverse to calculate log()
audio4 = np.where(audio3 < 0, (1/audio3) * -1, audio3)

#Convert values from amplitude to dB
audio_db = pd.DataFrame(20 * np.log10(audio4))
#audio_db = audio_db[audio_db != ]

#Filter out dB not in 
audio_voice = audio_db.loc[(audio_db[0] <= 60) & (audio_db[0] >= 20)]


#Length of instruction
sec_instruct = len(audio_voice) / (input_data[0])


#length of video in seconds                                
video_1_length = len(input_data[1]) / (input_data[0])


#Percent of time instructing
perc_instruct = (sec_instruct / video_1_length) * 100

#video_1_volume = audio.tolist()
#print(video_1_volume[0:5])



# plot the [] designated frames
#plt.plot(audio[0:1000])
# label the axes
#plt.ylabel("Amplitude")
#plt.xlabel("Time")
# set the title  
#plt.title("Sample Wav")
# display the plot
#plt.show()


