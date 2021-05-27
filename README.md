this is some new text

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

** Classifications **

	** Original work **
		
		** vids123 **
			Three original qualitative labels and three files indicating the output of proofreading.
		
		** vids456 **
			Three original qualitative label files, one file indicating proofreading, and three final qualitative label files.
			
	** Classifications_Vids123 **
		Final qualitative classifications in excel format for first three videos **
		
	** Classifications_Vids456 **
		Final qualitative classifications in excel format for second three videos **
		
	** codebook **
		Final draft of codebook used to conduct qualitative coding, proofread by external collaborators

** Video Analysis **

	** Audio **
		
		** ground_truth_speaking_vs_not **
			six .txt files indicating the ground truth time ranges in which a person was speaking
			
		** original_without_ads **
			six audio files of the workouts, after advertisements were removed. These were recorded using Audacity.
			
		** post_spleeter **
			six folders containing the "vocals" and "accompaniment" audio files after running the original workout file through spleeter.
			
	** Scripts **
	
		- amplify.py 					{Amplifies a WAV file by a given scaling factor - a potential approach}
										Github doc: https://github.com/russellcardullo/python-dsp/blob/master/amplify.py
		- Graph_Audio.py				{Graphs a WAV file, uses 1:00-1:10. Longer duration produces ugly plot}

		- Labels_Percent.py 			{Gives percent of instruction based of labels exported from audacity}

		- Percent_of_Instruction.py 	{Finds Percent of Instruction from a Wav import, dB threshold TBD}

		- silence_remove.py 			{a program that silences sound below a threshold generated with ML - a potential approach}
										Github doc: https://github.com/ngbala6/Audio-Processing/blob/master/Silence-Remove/silenceremove.py
		- sox_documentation.txt			code documentation to find the length of a video
		
		- spleeterNotes.txt				notes on how to run spleeter
		
		- test_parser.py				original code that gave an example of parsing text using nltk library
		
	** Transcripts **
		
		- VideoInformation: 			Link, Views, Date Posted, Video Length, Words Per Minute
		
		- Video_#						transcript of workout

** Percentage of Instruction **			Percentage of Instruction, Runs through percent_of_instruct.py with different dB thresholds (ignore kappa)

** Graphs **							Graphs of dB's of each video at different time increments

Considerations:
- Whether we accept breathing as "instruction": When the instructor uses a mic, spleeter labels breathing as vocals