from flask import Flask, render_template, request, jsonify, url_for, send_file
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_spectrogram', methods=['POST'])
def generate_spectrogram():
    # Get the audio file from the request
    file = request.files['audio_file']
    y, sr = librosa.load(file, sr=8000)

    # Extract mel spectrogram with increased resolution
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=256, hop_length=256)

    # Convert to decibels
    S_dB = librosa.power_to_db(S, ref=np.max)
 
    # Create a plot for the mel spectrogram
    plt.figure(figsize=(8, 5))
    librosa.display.specshow(S_dB, sr=sr, hop_length=256, x_axis='time', y_axis='mel', cmap='inferno')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel Spectrogram')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')

    # Save the plot to a BytesIO object
    img_stream = io.BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)

    # Send the image as a response with download prompt
    return send_file(img_stream, mimetype='image/png', as_attachment=True, download_name='spectrogram.png')

# New route for About ALS page
@app.route('/about')
def about_als():
    return render_template('about.html')  # Render About ALS page template

# New route for ALS Awareness page
@app.route('/als_awareness')
def als_awareness():
    return render_template('als_awareness.html')  # Render ALS Awareness page template

# New route for ALS Awareness page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)