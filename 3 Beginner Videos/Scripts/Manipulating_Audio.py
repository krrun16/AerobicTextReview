from scipy.io.wavfile import read
#import matplotlib.pyplot as plt
import numpy as np
import wave

# read audio samples using frame rate and # of frames
input_data = read("C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Calvin_Videos/Video 1/vocals.wav")

# extract solely the frames clipped
audio = input_data[1]

#Delete the second repetitive column
audio = np.delete(audio, [1,1])

#Change negative values to positive inverse to calculate log()
audio_inverse = np.where(audio < 0, (1/audio) * -1, audio)

#Convert values from amplitude to dB
audio_db = 20 * np.log10(audio_inverse)

#Filter out dB not in 
audio_voice = audio[audio < 60]

#Open file in audio format
video_1 = wave.open("C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Calvin_Videos/Video 1/vocals.wav")


#Find parameters in videos
video_1_params = video_1.getparams()


#Find of Length of Video solely from Code in seconds:
video_1_length = video_1_params[3] / video_1_params[2]


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


