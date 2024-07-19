import librosa
import matplotlib.pyplot as plt
import librosa.display

# array为音频文件,已元素的形式被加载
# sampling_rate为采样率
array, sampling_rate = librosa.load(librosa.ex("trumpet"))
plt.figure().set_figwidth(12)
librosa.display.waveshow(array, sr=sampling_rate)
plt.show()
print(array)
print(len(array))
print(sampling_rate)
