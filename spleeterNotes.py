"""
Spleeter Notes

Documentation
https://github.com/deezer/spleeter/blob/master/README.md

Spleeter install
[General]
# install using conda
conda config --add channels conda-forge # only needed if you don't already have this channel set
conda install -c deezer-research spleeter

[Windows]
Use complete Anaconda Installation; or manually install ffmpeg

[MAC]
conda install ffmpeg libsndfile
pip install spleeter


Terminal Command
spleeter separate -p spleeter:2stems -o spleeter_run/audio_output -i (file path)

Example:
spleeter separate -p spleeter:2stems -o spleeter_run/audio_output -i /Users/morgandeneve/Spleeter_test/audio_example.mp3

Terminal Command (More than 10 mins)
spleeter separate -p spleeter:2stems -o spleeter_run/audio_output -i [file path] -d [duration length in seconds]

Example:
spleeter separate -p spleeter:2stems -o spleeter_run/audio_output -i /Users/morgandeneve/spleeter_run/MadFit_NoiseReduced.mp3 -d 1074


Errors
Windows spleeter error
replace spleeter separate by python -m spleeter separate in command line

Issue locating directory or file path
Windows:
pressing control+shift and then right clicking on the file, and said "copy as path"
Mac:
right clicking on the file then pressing option+shift and clicking on "copy as path"


NotImplemented: cannot convert a symbolic tensor
“NotImplementedError: Cannot convert a symbolic Tensor (strided_slice_4:0) to a numpy array.”
Numpy Version Check
Terminal >> Python
Python 3.7.4 (default, Aug 13 2019, 15:17:50)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type “help”, “copyright”, “credits” or “license” for more information.
>>> import numpy
>>> numpy.version.version
‘1.20.1’
(numpy 1.20 or above does not work, need numpy 1.19.5 to work)
https://stackoverflow.com/questions/58479556/notimplementederror-cannot-convert-a-symbolic-tensor-2nd-target0-to-a-numpy

"""
