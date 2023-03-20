import sys
import soundfile as sf
import numpy as np
from scipy.fftpack import fft, fftfreq
from scipy.signal import decimate


def freq(path):
    data, _ = sf.read(path)
    if data.ndim > 1:
        data = np.mean(data, axis=1)
    data = decimate(data,8)
    data = np.pad(data, (0, 2**int(np.ceil(np.log2(len(data)))) - len(data)), 'constant')
    fft_data = fft(data)
    frequencies = np.abs(fft_data)[:len(fft_data)//2]
    #max_index = np.argmax(frequencies)
    #fundamental_frequency = fftfreq(len(data), 1/22050)[max_index]
    #print(f"fundamental freq: {fundamental_frequency}")
    if np.mean(frequencies[0:360]) > np.mean(frequencies[360:880]):
        return "K"
    else:
        return "M"

def testowanie():
    M =0
    K=0
    cM =0
    cK =0
    x = 1
    for i in range(1, 94):
        if i < 10:
            try:
                if freq(rf".\trainall\00{i}_K.wav") == "K":
                    K += 1
                cK += 1
            except:

                if freq(rf".\trainall\00{i}_M.wav") == "M":
                    M += 1
                cM += 1
            finally:
                pass
        else:
            try:
                if freq(rf".\trainall\0{i}_K.wav") == "K":
                    K += 1
                cK += 1
            except:
                if freq(rf".\trainall\0{i}_M.wav") == "M":
                    M += 1
                cM += 1
            finally:
                pass
    print(f"Wykryto M: {M}/{cM} oraz K: {K}/{cK}, co daje: {round((M+K)/(cM+cK) * 100,2)}% ")


try:
    path = sys.argv[1]
    print(freq(path))
except:
    print('Path incorrect!')
