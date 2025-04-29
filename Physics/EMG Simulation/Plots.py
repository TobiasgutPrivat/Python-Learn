from matplotlib import pyplot as plt
import numpy as np

def showEMGPlot(emg: list[np.ndarray],t):
    plt.figure(figsize=(12, 6))
    for i in range(len(emg)):
        plt.plot(t, emg[i], label=f'EMG Signal {i+1}')
    # plt.plot(t, emg, label='EMG Signal')
    plt.title('Simulated EMG Signal with Decreasing Frequency')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()
    plt.show()

def showAmpFreqPlot(emg_freq, emg_fft):
    plt.figure(figsize=(12, 6))
    plt.plot(np.abs(emg_freq), np.abs(emg_fft), label='EMG Signal')
    plt.title('Simulated EMG Signal with Decreasing Frequency')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()
    plt.show()

def showPSDPlot(freq, power):
    pos_freqs = freq > 0
    plt.figure(figsize=(10, 5))
    plt.plot(freq[pos_freqs], power[pos_freqs])
    plt.title("Power Spectrum (via FFT)")
    plt.xlabel("Frequenz (Hz)")
    plt.ylabel("Leistung")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def showPSDPlotWelch(frequencies, psd):
    plt.figure(figsize=(10, 5))
    plt.semilogy(frequencies, psd)
    plt.title("Leistungsspektrum (Power Spectrum) des EMG-Signals")
    plt.xlabel("Frequenz (Hz)")
    plt.ylabel("Leistung / Hz")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def showPSDPlotWelchAndMedian(frequencies, psd, median_freq):
    plt.figure(figsize=(10, 6))
    plt.semilogy(frequencies, psd, label="Powerspektrum")
    plt.axvline(median_freq, color='r', linestyle='--', label=f"Medianfrequenz ≈ {median_freq:.2f} Hz")
    plt.title("Powerspektrum und Medianfrequenz des EMG-Signals")
    plt.xlabel("Frequenz (Hz)")
    plt.ylabel("Leistung / Hz (log)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def showMedianFreqPlot(median_freqs, num_windows, window_duration):
    plt.figure(figsize=(8, 5))
    time_axis = np.arange(1, len(median_freqs) + 1) * window_duration
    plt.plot(time_axis, median_freqs, marker='o')
    plt.title("Verlauf der Medianfrequenz über Zeit (Muskelermüdung)")
    plt.xlabel("Zeit (s)")
    plt.ylabel("Medianfrequenz (Hz)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()