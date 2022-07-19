'''
Authors  
Paul Moses Mulwa
Timothy Ndichu
'''
import os
import wave
import numpy as np
import matplotlib.pyplot as plt


# PART ONE
TOP_DIR = os.path.dirname(os.path.abspath(__file__)) #get current path of file
fname = os.path.join(TOP_DIR, "StarWars60.wav")

'''------------------------------------------------------------
Wavefile operations

Wave_read objects, as returned by open(), have the following methods:

Wave_read.close()
Close the stream if it was opened by wave, and make the instance unusable. This is called automatically on object collection.

Wave_read.getnchannels()
Returns number of audio channels (1 for mono, 2 for stereo).

Wave_read.getsampwidth()
Returns sample width in bytes.

Wave_read.getframerate()
Returns sampling frequency.

Wave_read.getnframes()
Returns number of audio frames.

Wave_read.getcomptype()
Returns compression type ('NONE' is the only supported type).

Wave_read.getcompname()
Human-readable version of getcomptype(). Usually 'not compressed' parallels 'NONE'.

Wave_read.getparams()
Returns a namedtuple() (nchannels, sampwidth, framerate, nframes, comptype, compname), equivalent to output of the get*() methods.

Wave_read.readframes(n)
Reads and returns at most n frames of audio, as a bytes object.

-------------------------------------------------
'''


wav = wave.open(fname, 'r')
# -----------------------------------------------------------
num_channels = wav.getnchannels()
print("The number of channels is ",num_channels)
# -----------------------------------------------------------
num_frames = wav.getnframes()
print("The number of frames is ",num_frames)
# -----------------------------------------------------------
frameRate = wav.getframerate()
print("The frame rate is ",frameRate)
# -----------------------------------------------------------
sampleWidth = wav.getsampwidth()
print("The sample width is ",sampleWidth)
# -----------------------------------------------------------
raw = wav.readframes(-1) #get all the frames
raw = np.frombuffer(raw, "int16") #Interpret a buffer as a 1-dimensional array.

'''The NumPy linspace function 
(sometimes called np.linspace) is a tool in Python for creating numeric sequences.

Essentally, you specify a starting point and an ending point of an interval, 
and then specify the total number of breakpoints you want within that interval
(including the start and end points). 
The np.linspace function will return a sequence of evenly spaced values on that interval.

np.linspace(start = 0, stop = 100, number_of_intervals = 5)
'''
time = np.linspace(0, len(raw)/frameRate, num=len(raw))

fig = plt.figure()
axis = fig.add_subplot(111)
fig.suptitle('Wavefile plot')
axis.plot(time, raw, color='blue', linewidth=0.2)
plt.ylabel('Amplitude')
plt.show()
