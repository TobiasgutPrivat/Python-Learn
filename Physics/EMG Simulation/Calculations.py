import numpy as np
from scipy.signal import welch

# 1. Calculate Power Spectral Density (PSD)
def compute_psd(signal, fs, nperseg=1024):
    freqs, psd = welch(signal, fs=fs, nperseg=nperseg)
    return freqs, psd

# 2. Calculate Median Frequency from PSD
def compute_median_frequency(freqs, psd):
    cumulative_power = np.cumsum(psd)
    total_power = cumulative_power[-1]
    median_index = np.where(cumulative_power >= total_power / 2)[0][0]
    return freqs[median_index]

# 3. Calculate Median Frequencies for Windowed Segments
def compute_median_frequencies_over_time(signal, fs, window_duration):
    samples_per_window = int(fs * window_duration)
    num_windows = len(signal) // samples_per_window
    median_freqs = []

    for i in range(num_windows):
        start = i * samples_per_window
        end = start + samples_per_window
        segment = signal[start:end]
        
        freqs, psd = compute_psd(segment, fs)
        median_freq = compute_median_frequency(freqs, psd)
        median_freqs.append(median_freq)

    return median_freqs
