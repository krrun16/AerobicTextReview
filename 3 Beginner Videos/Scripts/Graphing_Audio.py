#from scipy.io.wavfile import read
#import matplotlib.pyplot as plt
 

# read audio samples
#input_data = read("C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Calvin_Videos/Video 1/vocals.wav")
#audio = input_data[1]
#instruction = audio.index[audio > 0]

# plot the [] designated samples
#plt.plot(audio[1000:10000])

# label the axes
#plt.ylabel("Amplitude")
#plt.xlabel("Time")
# set the title  
#plt.title("Sample Wav")
# display the plot
#plt.show()


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
  
# shows the sound waves
def visualize(path: str):
    
    # reading the audio file
    raw = wave.open(path)
      
    # reads all the frames 
    # -1 indicates all or max frames
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")
      
    # gets the frame rate
    f_rate = raw.getframerate()
  
    # to Plot the x-axis in seconds 
    # you need get the frame rate 
    # and divide by size of your signal
    # to create a Time Vector 
    # spaced linearly with the size 
    # of the audio file
    time = np.linspace(
        0, # start
        len(signal) / f_rate,
        num = len(signal)
    )
  
    # using matlplotlib to plot
    # creates a new figure
    plt.figure(1)
      
    # title of the plot
    plt.title("Sound Wave")
      
    # label of x-axis
    plt.xlabel("Time")
     
    # actual ploting
    plt.plot(time, signal)
      
    # shows the plot 
    # in new window
    plt.show()
  
    # you can also save
    # the plot using
    # plt.savefig('filename')
  
  
if __name__ == "__main__":
    
    # gets the command line Value
    path = sys.argv[1]
  
    visualize(path)