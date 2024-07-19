# 										audio

## 时域与频域的关系

![](D:\截屏\390f13d2c5522c540cddc4d27e07b0eb.jpg)

一个时间点的声音由多种不同频率的声波组成,

以时间为量度(就是从红色区向右看)就是时域,此时做出来的图横坐标为时间,纵坐标为振幅(幅值),物理意义为这段时间轴上声音的总体振幅(幅值)变化

以频率为量度,也就是只分析一个时间点或者很短的时间(从蓝色区域向左看),就是频域,此时横坐标为频率,纵坐标为振幅(幅值),物理意义为这段短时间内不同频率的声波的振幅(幅值)

时域到频域可以通过离散傅里叶变换(DFT)实现,也可逆转化

也可通过短时傅里叶变化(STFT的本质就是将一段信号截成多段，对每一段进行单独傅里叶变换（FFT），最后在时域上接起来，就形成了STFT的结果)将时域图与频域图融合为时域图(详见下文)

  (个人理解)



## 音频的波形表示(时域)

![](D:\py\projects\audio\unit1\part1\plots\波形图.png)

​								横坐标是时间,纵坐标是幅值

在librosa中,幅值以浮点数返回,数值在[-1,1]中

```python
import librosa
import matplotlib.pyplot as plt
import librosa.display

# array为音频文件,已元素的形式被加载
# sampling_rate为采样率
# 这里的"trumpet"为librosa中自带的数据集
array, sampling_rate = librosa.load(librosa.ex("trumpet"))
plt.figure().set_figwidth(12)
# 使用librosa的函数自动绘制波形图
librosa.display.waveshow(array, sr=sampling_rate)
plt.show()
print(array)
print(len(array))
print(sampling_rate)
```

输出

![](D:\截屏\Snipaste_2024-07-12_21-30-08.png)







## 频域

![](D:\py\projects\audio\unit1\part1\plots\频谱图.png)

​													横坐标为频率,纵坐标为响度(dB)

振幅可以转化为响度,公式如下

![](D:\截屏\Snipaste_2024-07-12_21-36-00.png)



```python
import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np

# array为音频文件,已元素的形式被加载
# sampling_rate为采样率
array, sampling_rate = librosa.load(librosa.ex("trumpet"))
# 频域计算选取一小段时间,这里大概为一个音符的长度
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
# 将 x 轴设置为对数刻度,原因见上图公式
plt.xscale("log")

plt.show()
```





## 时频图

![](D:\py\projects\audio\unit1\part1\plots\时频图.png)

​			横坐标为时间,纵坐标为频率,通过不同的颜色区分响度

注意区分 时频图与时域图和频域图的区别(时频图是两者的结合)



此为上文中的时域图

![](D:\py\projects\audio\unit1\part1\plots\波形图.png)

此为上文中的频域图

![](D:\py\projects\audio\unit1\part1\plots\频谱图.png)

```python
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
```



## 梅尔谱

一种时频谱变体，与标准时频谱相比，梅尔谱可以捕捉更多人类可感知的音频特征

标准时频谱的频率(y轴)是赫兹的线性变化。 由于人类听觉系统对于低频率声音的变化更敏感，对于高频率声音的变化则较不敏感。这一敏感度的变化是随频率的上升呈对数关系下降的

在此不过多分析



![](D:\py\projects\audio\unit1\part1\plots\梅尔图.png)



```python
import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np

# array为音频文件,已元素的形式被加载
# sampling_rate为采样率
array, sampling_rate = librosa.load(librosa.ex("trumpet"))
S = librosa.feature.melspectrogram(y=array, sr=sampling_rate, n_mels=128, fmax=8000)
S_dB = librosa.power_to_db(S, ref=np.max)

plt.figure().set_figwidth(12)
librosa.display.specshow(S_dB, x_axis="time", y_axis="mel", sr=sampling_rate, fmax=8000)
plt.colorbar()

plt.show()
```

