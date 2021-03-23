from pydub import AudioSegment
from pydub.playback import play


#Changing format from MP3 to Wav
vid_1_src = "C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Videos/Video_1_trimmed.mp3"

vid_1_dst = "C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Videos/Video_1_trimmed.wav"

sound_vid_1 = AudioSegment.from_mp3(vid_1_src)
sound_vid_1.export(vid_1_dst, format="wav")
sound_vid_1 = AudioSegment.from_wav(vid_1_dst)

#Length in Seconds
vid_1_duration = (len(sound_vid_1)/1000)
print(vid_1_duration)


#vid_1 = AudioSegment.from_file("C:/Users/calvi/OneDrive - University of Iowa/Documents/aerobictextreview/3 Beginner Videos/Videos/Video_1_trimmed.wav")
