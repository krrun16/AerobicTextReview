import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import pandas as pd
import numpy as np
import sys

filename = sys.argv[1]
#"C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/videos/video_2/vocals.wav"

# read audio samples using frame rate and # of frames
input_data = read(filename)
# extract solely the frames clipped
audio = pd.DataFrame(input_data[1])    

#Change negative values to positive inverse to calculate log()
audio = np.where(audio < 0, (1/audio) * -1, audio)
    
#Convert values from amplitude to dB
audio_db = pd.DataFrame(20 * np.log10(audio))


# plot the [] designated frames
# to find the seconds of video indexed, divide by frame rate
plt.plot(audio_db[2646000:3087000])
plt.ylabel("dB")
plt.xlabel("Time")

# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()
