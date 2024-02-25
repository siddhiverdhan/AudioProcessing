import sys
import numpy as np
import config
import librosa

np.set_printoptions(threshold=sys.maxsize)

filename = config.testfilelocation
Fs = 44100
clip, sample_rate = librosa.load(filename, sr=Fs)

n_fft = 1024  # frame length
start = 0

hop_length=512

#commented out code to display Spectrogram
X = librosa.stft(clip, n_fft=n_fft, hop_length=hop_length)
#Xdb = librosa.amplitude_to_db(abs(X))
#plt.figure(figsize=(14, 5))
#librosa.display.specshow(Xdb, sr=Fs, x_axis='time', y_axis='hz')
#If to pring log of frequencies
#librosa.display.specshow(Xdb, sr=Fs, x_axis='time', y_axis='log')
#plt.colorbar()

#librosa.display.waveplot(clip, sr=Fs)
#plt.show()

#now print all values

t_samples = np.arange(clip.shape[0]) / Fs
t_frames = np.arange(X.shape[1]) * hop_length / Fs
#f_hertz = np.arange(N / 2 + 1) * Fs / N       # Works only when N is even
f_hertz = np.fft.rfftfreq(n_fft, 1 / Fs)         # Works also when N is odd

#example
print('Time (seconds) of last sample:', t_samples[-1])
print('Time (seconds) of last frame: ', t_frames[-1])
print('Frequency (Hz) of last bin:   ', f_hertz[-1])

print('Time (seconds) :', len(t_samples))

#prints array of time frames
print('Time of frames (seconds) : ', t_frames)
#prints array of frequency bins
print('Frequency (Hz) : ', f_hertz)

print('Number of frames : ', len(t_frames))
print('Number of bins : ', len(f_hertz))

#This code is working to printout frame by frame intensity of each frequency
#on top line gives freq bins
curLine = 'Bins,'
for b in range(1, len(f_hertz)):
    curLine += str(f_hertz[b]) + ','
print(curLine)

curLine = ''
for f in range(1, len(t_frames)):
    curLine = str(t_frames[f]) + ','
    for b in range(1, len(f_hertz)): #for each frame, we get list of bin values printed
        curLine += str("%.02f" % np.abs(X[b, f])) + ','
        #remove format of the float for full details if needed
        #curLine += str(np.abs(X[b, f])) + ','
        #print other useful info like phase of frequency bin b at frame f.
        #curLine += str("%.02f" % np.angle(X[b, f])) + ','
    print(curLine)


