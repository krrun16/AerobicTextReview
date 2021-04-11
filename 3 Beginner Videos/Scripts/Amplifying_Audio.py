from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
input_data = read("C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Videos/audio_output/Video_1_trimmed/vocals_loudnorm.wav")
audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio[0:1024])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()
