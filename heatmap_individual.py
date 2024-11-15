import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display

# Load the audio file
y, sr = librosa.load("C:/Users/Priyamvadha Pradeep/Desktop/FYP/heatmap code/fyp_dataset/fyp_dataset/phonation_a/CT001_phonationA.wav", sr=None)

# Extract mel spectrogram with increased resolution
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=256, hop_length=256)

# Convert to decibels
S_dB = librosa.power_to_db(S, ref=np.max)

# Plot the mel spectrogram
plt.figure(figsize=(12, 8))
librosa.display.specshow(S_dB, sr=sr, hop_length=256, x_axis='time', y_axis='mel', cmap='inferno')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()

# Customize and save the heatmap
plt.figure(figsize=(12, 8))
librosa.display.specshow(S_dB, sr=sr, hop_length=256, x_axis='time', y_axis='mel', cmap='inferno')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

# Save the heatmap to a file
plt.savefig('mel_spectrogram_heatmap_clear.png')