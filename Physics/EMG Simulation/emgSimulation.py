# create a simulation of EMG signals representing muscle activity decreasing over time due to fatigue
import numpy as np
import matplotlib.pyplot as plt
from Plots import showEMGPlot, showAmpFreqPlot, showPSDPlot, showPSDPlotWelch, showPSDPlotWelchAndMedian, showMedianFreqPlot
from Filters import moving_average, butter_lowpass_filter, butter_bandpass_filter
from scipy.signal import welch

fs = 1000  # Sampling frequency in Hz
T = 30  # % Duration in seconds
t = np.arange(0, T, 1/fs)  # Time vector

freqs = np.linspace(100, 40, len(t))  # Frequency vector

clearEMG = np.sin(2 * np.pi * freqs * t) # Simulated EMG signal
noise = 0.5 * np.random.randn(len(t))  # Random noise
emg = clearEMG + noise # Simulated EMG signal + noise

# filter out noise
# emg_filtered = moving_average(emg, window_size=100)
emg_filtered = butter_lowpass_filter(emg, cutoff=100, fs=fs)
# emg_filtered = butter_bandpass_filter(emg, lowcut=40, highcut=100, fs=fs)

# showEMGPlot([emg,emg_filtered,clearEMG,clearEMG-emg_filtered], t)

#get amplitude frequency domain
emg_fft = np.fft.fft(emg_filtered)
emg_freq = np.fft.fftfreq(len(emg_filtered), 1/fs)  # Frequency vector for FFT

#displey frequency domain
# showAmpFreqPlot(emg_freq, emg_fft)

# calculate Power Spectral Density (PSD)

# power = np.abs(emg_fft)**2 / len(emg_filtered)
frequencies, psd = welch(emg_filtered, fs=fs, nperseg=1024)

# median frequency
cumulative_power = np.cumsum(psd)
total_power = cumulative_power[-1]
median_freq_index = np.where(cumulative_power >= total_power / 2)[0][0]
median_freq = frequencies[median_freq_index]

# display PSD
# showPSDPlotWelchAndMedian(frequencies, psd, median_freq)

# calculate median frequency for each window
window_duration = 5  # Sekunden
samples_per_window = int(fs * window_duration)
num_windows = int(len(emg_filtered) / samples_per_window)

median_freqs = []

for i in range(num_windows):
    start = i * samples_per_window
    end = start + samples_per_window
    emg_segment = emg_filtered[start:end]
    
    # PSD berechnen
    freqs, psd = welch(emg_segment, fs=fs, nperseg=1024)
    
    # Medianfrequenz berechnen
    cumulative_power = np.cumsum(psd)
    total_power = cumulative_power[-1]
    median_index = np.where(cumulative_power >= total_power / 2)[0][0]
    median_freq = freqs[median_index]
    
    median_freqs.append(median_freq)

showMedianFreqPlot(median_freqs, window_duration, num_windows)