import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np

# array为音频文件,已元素的形式被加载
# sampling_rate为采样率
array, sampling_rate = librosa.load(librosa.ex("trumpet"))

# 短时傅里叶变化
# STFT的本质就是将一段信号截成多段，对每一段进行单独傅里叶变换（FFT），最后在时域上接起来，就形成了STFT的结果
D = librosa.stft(array)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

plt.figure().set_figwidth(12)
librosa.display.specshow(S_db, x_axis="time", y_axis="hz")
plt.colorbar()

plt.show()
