import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np

# array为音频文件,已元素的形式被加载
# sampling_rate为采样率
array, sampling_rate = librosa.load(librosa.ex("trumpet"))
dft_input = array[:4096]
# 计算DFT
window = np.hanning(len(dft_input))
windowed_input = dft_input * window
dft = np.fft.rfft(windowed_input)

# 计算频谱的幅值,转换为分贝标度
amplitude = np.abs(dft)
amplitude_db = librosa.amplitude_to_db(amplitude, ref=np.max)

# 计算每个DFT分量对应的频率值
frequency = librosa.fft_frequencies(sr=sampling_rate, n_fft=len(dft_input))

plt.figure().set_figwidth(12)
# 绘制频率和幅度之间的关系曲线
plt.plot(frequency, amplitude_db)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dB)")
# 将 x 轴设置为对数刻度
plt.xscale("log")

plt.show()
