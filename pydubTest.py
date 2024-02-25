import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import config

# Import the .wav audio
file = config.testfilelocation
# s = sampling (int)
# a = audio signal (numpy array)
sampleRate, audio = wavfile.read(file)
print('Sampling Rate:' , sampleRate)
print('Audio Shape:' , np.shape(audio))

#number of samples
na = audio.shape[0]
#audio time duration
la = na / sampleRate

#plot signal versus time
t = np.linspace(0,la,na)
plt.subplot(2,1,1)
plt.plot(t,audio[:,0],'b-')
plt.ylabel('Left')
plt.subplot(2,1,2)
plt.plot(t,audio[:,1],'r-')
plt.ylabel('Right')
plt.xlabel('Time (s)')
plt.show()

### Fast Fourier
a_k = np.fft.fft(audio)[0:int(na/2)]/na # FFT function from numpy
a_k[1:] = 2*a_k[1:] # single-sided spectrum only
Pxx = np.abs(a_k)   # remove imaginary part
f = sampleRate*np.arange((na/2))/na # frequency vector

#plotting
fig,ax = plt.subplots()
plt.plot(f,Pxx,'b-',label='Audio Signal')
plt.plot([20,20000],[0.1,0.1],'r-',alpha=0.7, \
         linewidth=10,label='Audible (Humans)')
ax.set_xscale('log'); ax.set_yscale('log')
plt.grid(); plt.legend()
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')
plt.show()