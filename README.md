# aerobictextreview

Analyze text from aerobics workouts to determine whether the phrases are helpful or confusing

Getting started:

With the following notes, I am referring to directions on https://www.nltk.org/install.html, but read my notes below before beginning.
1. Make sure you have python installed on your computer: https://www.python.org/downloads/
2. I recommend installing anaconda to maintain python environments, like it is suggested on the webpage.
3. Contrary to what it says, you can run the "Mac/Unix" instructions on a Windows machine. To do so, run "Anaconda prompt" (after installing anaconda mentioned above). You will get a terminal window. Complete the "Mac/Unix" instructions in that terminal. #2 I would install numpy.
4. After completing step #3 in the "Mac/Unix" instructions, scroll down to "Installing NLTK Data."

Then, you can follow this tutorial to install nltk packages and run basic text analysis. This should give us the foundation to get started: https://likegeeks.com/nlp-tutorial-using-python-nltk/

It is fine if you explore these things and keep the code out of this repository. But when we start writing code for the project, make sure you are in your anaconda environment with everything installed. I added a file I was using along with the tutorial to .gitignore so that I could keep it around, but not have it pushed.


**TABLE OF CONTENTS:** 

**--> 3 Beginner Videos**

**3 Beginner videos\Videos**

Video_#: 
- 	accompaniment.wav 		<Music from using spleeter>
- 	vocals.wav 				<Vocals from using spleeter>	
- 	video_#.mp3 			<original recording in audacity>
- 	EDITED_LEGIT_LABELS 	<labeled timestamp durations of sound detected in video>
	

**3 Beginner videos\scripts**
- Amplify.py 					{Amplifies a WAV file by a given scaling factor - a potential approach}
Github doc: https://github.com/russellcardullo/python-dsp/blob/master/amplify.py

- Graph_Audio.py				{Graphs a WAV file, uses 1:00-1:10. Longer duration produces ugly plot}

- Labels_Percent.py 			{Gives percent of instruction based of labels exported from audacity}

- Percent_of_Instruction.py 	{Finds Percent of Instruction from a Wav import, dB threshold TBD}

- Silence_Remove.py 		{a program that silences sound below a threshold generated with ML - a potential approach}
Github doc: https://github.com/ngbala6/Audio-Processing/blob/master/Silence-Remove/silenceremove.py



**3 Beginner videos\Transcripts**
- Video_#: 			<Link, Views, Date Posted, Video Length, Words Per Minute, and transcript>


**3 Beginner Videos**

- Percentage of Instruction: 	<Actual Percentage of Instruction, Runs through percent_of_instruct.py with different dB thresholds. >


- Graphs						<Graphs of dB's of each video at different time increments>




CONCERNS TO THINK ABOUT:

Detecting heavy breathing as instruction or not: can manually detect in audacity, but not sure what the python 
	script will do. 

-- I think when an instructor uses a mic it detects a lot of breathes as instruction
