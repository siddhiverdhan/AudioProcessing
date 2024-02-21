import librosa
from config import config
import matplotlib.pyplot as plt
from dtw import dtw

filename1 = config.testfilelocation1
filename2 = config.testfilelocation2
# Load the two audio files
y1, sr1 = librosa.load('/Users/prashanthprabhu/Documents/GitHub/AudioProcessing/audiofiles/Adver.wav')
y2, sr2 = librosa.load('/Users/prashanthprabhu/Documents/GitHub/AudioProcessing/audiofiles/Adver.wav')

# Extract the MFCC features from each audio file
mfcc1 = librosa.feature.mfcc(y = y1, sr = sr1)
mfcc2 = librosa.feature.mfcc(y = y2, sr = sr2)

#librosa.feature.mfcc()
# Compute the distance between the two sets of features
#distance = librosa.distance.cosine(mfcc1, mfcc2)

dist, cost, path = dtw(mfcc1.T, mfcc2.T)
# Print the distance
print(dist)

# Visualize the MFCC features
plt.figure(figsize=(10, 4))
librosa.display.mfcc(mfcc1)
plt.colorbar()
plt.title('MFCC Features')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()