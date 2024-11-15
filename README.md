# Early-Detection-of-ALS-using-Speech-Analysis-and-Neural-Networks

# Speech Analysis for ALS Detection

This project provides an interactive web application that analyzes voice samples to detect early signs of Amyotrophic Lateral Sclerosis (ALS) through speech analysis. It generates Mel Spectrograms and extracts acoustic features from uploaded audio files to aid in ALS detection.

## Features

- **Upload Audio**: Users can upload audio files (.wav format) for analysis.
- **Generate Spectrogram**: The app generates a Mel spectrogram from the uploaded audio file, which is a graphical representation of the frequency spectrum over time.
- **Download Spectrogram**: After the spectrogram is generated, users can download the image as a PNG file.
- **Acoustic Feature Analysis**: The app provides an option to analyze the acoustic features of the uploaded audio, such as pitch, jitter, shimmer, and Harmonics-to-Noise Ratio (HNR).
- **ALS Detection**: Future integration with machine learning models for ALS detection based on speech characteristics.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/als-speech-analysis.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` file includes necessary libraries like Flask, librosa, and matplotlib.

3. Start the Flask application:
   ```bash
   python app.py
   ```
   The app will be hosted locally at `http://127.0.0.1:5000`.

## Usage

- **Home Page**: The home page allows users to upload a `.wav` audio file. Once the file is selected, the user can generate a Mel spectrogram, analyze acoustic features, or run an ALS detection model.
- **Download Spectrogram**: After generating the spectrogram, you can download the image in PNG format.
- **About ALS**: The "About" page provides information on ALS and its symptoms.
- **ALS Awareness**: The "ALS Awareness" page shares important facts and statistics about ALS.
- **Contact Us**: Users can contact the development team through the "Contact Us" page.

## Technologies Used

- **Flask**: A micro web framework for Python, used to build the web application.
- **Librosa**: A Python package for analyzing and processing audio signals, used to generate the spectrogram.
- **Matplotlib**: A Python plotting library used to visualize the spectrogram.
- **HTML/CSS**: Used for structuring and styling the front-end pages.

## Disclaimer

This application is designed for educational and research purposes only. The results from speech analysis should not be considered as medical advice.
