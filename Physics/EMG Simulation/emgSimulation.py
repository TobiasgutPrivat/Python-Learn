# create a simulation of EMG signals representing muscle activity decreasing over time due to fatigue
import numpy as np
from Plots import showEMGPlot, showAmpFreqPlot, showPSDPlot, showPSDPlotWelch, showPSDPlotWelchAndMedian, showMedianFreqPlot
from Filters import moving_average, butter_lowpass_filter, butter_bandpass_filter
from Calculations import compute_psd, compute_median_frequency, compute_median_frequencies_over_time

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

# get amplitude frequency domain
emg_fft = np.fft.fft(emg_filtered)
emg_freq = np.fft.fftfreq(len(emg_filtered), 1/fs)  # Frequency vector for FFT

# display frequency domain
# showAmpFreqPlot(emg_freq, emg_fft)

# calculate Power Spectral Density (PSD)

# power = np.abs(emg_fft)**2 / len(emg_filtered)
freqs, psd = compute_psd(emg_filtered, fs)
median_freq = compute_median_frequency(freqs, psd)

# Example: median frequencies over time
window_duration = 5  # seconds
median_freqs = compute_median_frequencies_over_time(emg_filtered, fs, window_duration)

# showPSDPlot(freqs, power)
# showPSDPlotWelch(freqs, psd)
# showPSDPlotWelchAndMedian(freqs, psd, median_freq)
showMedianFreqPlot(median_freqs, len(median_freqs), window_duration)