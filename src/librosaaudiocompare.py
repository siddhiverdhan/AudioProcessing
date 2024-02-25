import librosa
from fastdtw import fastdtw


def compare_audio(filename1, filename2):
    # Load the two audio files
    y1, sr1 = librosa.load(filename1)
    y2, sr2 = librosa.load(filename2)

    return_dict = {}

    # Extract the features from each audio file
    mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1)
    mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2)
    chroma_stft1 = librosa.feature.chroma_stft(y=y1, sr=sr1)
    chroma_stft2 = librosa.feature.chroma_stft(y=y2, sr=sr2)
    spec_cent1 = librosa.feature.spectral_centroid(y=y1, sr=sr1)
    spec_cent2 = librosa.feature.spectral_centroid(y=y2, sr=sr2)
    spec_bw1 = librosa.feature.spectral_bandwidth(y=y1, sr=sr1)
    spec_bw2 = librosa.feature.spectral_bandwidth(y=y2, sr=sr2)
    rolloff1 = librosa.feature.spectral_rolloff(y=y1, sr=sr1)
    rolloff2 = librosa.feature.spectral_rolloff(y=y2, sr=sr2)
    zcr1 = librosa.feature.zero_crossing_rate(y1)
    zcr2 = librosa.feature.zero_crossing_rate(y2)

    # compare features
    dist, path = fastdtw(mfcc1.T, mfcc2.T)
    return_dict["mfcc"] = dist
    # Print the distance
    print("Distance MFCC is :- " + str(dist))

    dist, path = fastdtw(spec_cent1.T, spec_cent2.T)
    # Print the distance
    print("Distance SPCENT is :- " + str(dist))
    return_dict["spec_cent"] = dist

    dist, path = fastdtw(chroma_stft1.T, chroma_stft2.T)
    # Print the distance
    print("Distance Chroma Stft is :- " + str(dist))
    return_dict["chroma_stft"] = dist

    dist, path = fastdtw(spec_bw1.T, spec_bw2.T)
    # Print the distance
    print("Distance Spectral Bandwidth is :- " + str(dist))
    return_dict["spec_bw"] = dist

    dist, path = fastdtw(rolloff1.T, rolloff2.T)
    return_dict["roll_off"] = dist
    # Print the distance
    print("Distance roll off frequency is :- " + str(dist))

    return_dict["zero_cross_rate"] = dist
    dist, path = fastdtw(zcr1.T, zcr2.T)
    # Print the distance
    print("Distance zero crossing rate is :- " + str(dist))

    print(return_dict)
    return return_dict
