import librosa
import numpy as np
import matplotlib.pyplot as plt
import noisereduce as nr
import librosa.display
import soundfile as sf


def preprocessor(y, sr, top_db=17):
    # 使用 librosa 的函数来检测非静音区间
    non_silent_intervals = librosa.effects.split(y, top_db=top_db)
    # 从检测到的非静音区间中提取有效部分
    non_silent_audio = np.concatenate([y[start:end] for start, end in non_silent_intervals])
    # 去除噪音
    reduced_noise = nr.reduce_noise(y=non_silent_audio, sr=sr)
    return reduced_noise


def time_domain(file_path):
    array, sampling_rate = librosa.load(file_path)
    audio = preprocessor(array, sampling_rate, top_db=17)
    plt.figure().set_figwidth(12)
    librosa.display.waveshow(audio, sr=sampling_rate)
    plt.show()
    plt.savefig('时域.png')


def time_frequency_domain(file_path):
    # array为音频文件,已元素的形式被加载
    # sampling_rate为采样率
    array, sampling_rate = librosa.load(file_path)
    # array=array[:4096]
    array = preprocessor(array, sampling_rate, top_db=17)
    # 短时傅里叶变化
    # STFT的本质就是将一段信号截成多段，对每一段进行单独傅里叶变换（FFT），最后在时域上接起来，就形成了STFT的结果
    D = librosa.stft(array)
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    plt.figure().set_figwidth(12)
    librosa.display.specshow(S_db, x_axis="time", y_axis="hz")
    plt.colorbar()
    plt.show()
    plt.savefig('时频域.png')


def mel_domain(file_path):
    array, sampling_rate = librosa.load(file_path)
    array = preprocessor(array, sampling_rate, top_db=17)
    S = librosa.feature.melspectrogram(y=array, sr=sampling_rate, n_mels=128, fmax=8000)
    S_dB = librosa.power_to_db(S, ref=np.max)
    plt.figure().set_figwidth(12)
    librosa.display.specshow(S_dB, x_axis="time", y_axis="mel", sr=sampling_rate, fmax=8000)
    plt.colorbar()
    plt.show()
    plt.savefig('梅尔.png')


def frequency_domain(file_path):
    array, sampling_rate = librosa.load(file_path)
    array = preprocessor(array, sampling_rate, top_db=17)
    # dft_input = array
    dft_input = array
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
    plt.savefig('频域.png')


def save_audio(file_path):
    array, sampling_rate = librosa.load(file_path)
    array = preprocessor(array, sampling_rate, top_db=17)
    sf.write('audio.wav', array, sampling_rate)


def get_spectrogram(file_path):
    time_domain(file_path)
    time_frequency_domain(file_path)
    mel_domain(file_path)
    frequency_domain(file_path)
    save_audio(file_path)
