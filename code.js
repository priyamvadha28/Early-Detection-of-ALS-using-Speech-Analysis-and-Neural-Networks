function generateSpectrogram() {
    if (selectedFile) {
        const formData = new FormData();
        formData.append('file', selectedFile);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                outputDiv.innerHTML = data.error;
            } else {
                outputDiv.innerHTML = "Generating Spectrogram...";
                return fetch('/generate_spectrogram', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ file_path: data.file_path })
                });
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.spectrogram_path) {
                outputDiv.innerHTML = `<img src="${data.spectrogram_path}" alt="Spectrogram">`;
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please upload a WAV file.');
    }
}

function analyzeFeatures() {
    if (selectedFile) {
        outputDiv.innerHTML = "Analyzing Acoustic Features...";
        fetch('/analyze_features', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ file_path: selectedFile.name })
        })
        .then(response => response.json())
        .then(data => {
            outputDiv.innerHTML = `Features: ${JSON.stringify(data.features)}`;
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please upload a WAV file.');
    }
}

function runModel() {
    if (selectedFile) {
        outputDiv.innerHTML = "Running ALS Detection Model...";
        fetch('/run_model', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            outputDiv.innerHTML = data.message + ' Result: ' + data.result;
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please upload a WAV file.');
    }
}