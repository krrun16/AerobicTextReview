from scipy.io.wavfile import read
import matplotlib.pyplot as plt
 

# read audio samples
input_data = read("C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Calvin_Videos/Video 1/vocals.wav")
audio = input_data[1]

# plot the [] designated frames
plt.plot(audio[0:100])

print(len(audio))
print(audio[0:100])


# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
#plt.show()


import wave

video_1 = wave.open("C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Calvin_Videos/Video 1/vocals.wav")

#Find parameters in videos
video_1_params = video_1.getparams()


#Find of Length of Video solely from Code in seconds:
video_1_length = video_1_params[3] / video_1_params[2]

video_1_volume = audio.tolist()
print(video_1_volume[0:5])