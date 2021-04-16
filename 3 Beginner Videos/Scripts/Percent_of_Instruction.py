from scipy.io.wavfile import read
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys


def main():
    
    script = sys.argv[0]
    filename = sys.argv[1]
    
    # read audio samples using frame rate and # of frames
    input_data = read(filename)
       
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
    print(perc_instruct)
    
if __name__ == '__main__':
    main()