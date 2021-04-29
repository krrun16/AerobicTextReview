import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import pandas as pd
import sys


filename = sys.argv[1]


# read audio samples using frame rate and # of frames
input_data = read(filename)
# extract solely the frames clipped
audio = pd.DataFrame(input_data[1])    
   
# plot the [] designated frames
plt.plot(audio[0:10000])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()