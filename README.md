# NeuroScribe - Handwriting to OCR and Audio Generator

## Introduction
NeuroScribe is an AI-powered application designed to revolutionize the way you handle handwritten content. It allows users to either upload an image of handwritten text or draw directly on a canvas, converting the input into editable digital text and audio files using cutting-edge OCR technology and advanced machine learning algorithms.

## Features
- Upload an image or draw on a canvas to convert handwriting into digital text.
- Generate audio files from the recognized text.
- User-friendly interface with responsive design.
- High accuracy in text recognition, leveraging state-of-the-art OCR technology.

## Project Structure
```
NeuroScribe/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── upload_file.html
│   └── upload_canvas.html
├── static/
│   └── styles.css
├── requirements.txt
└── README.txt
```

## Setup Instructions

### Prerequisites
- Python 3.x
- Flask
- Tesseract OCR (installation guide below)
- pip (Python package installer)

### Installing Tesseract OCR
1. **Windows**:
   - Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
   - Run the installer and follow the setup instructions.
   - Add the Tesseract executable to your system's PATH.

2. **macOS**:
   - Install via Homebrew:
     ```sh
     brew install tesseract
     ```

3. **Linux**:
   - Install via package manager:
     ```sh
     sudo apt-get install tesseract-ocr
     ```

### Setting up the Project
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/SoninX/ocr-audio.git
   cd NeuroScribe
   ```

2. **Create a Virtual Environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application
1. **Start the Flask Application**:
   ```sh
   python app.py
   ```

2. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Using NeuroScribe

### Home Page
The landing page offers two options:
- **Upload an Image**: Navigate to a page where you can upload a handwritten image file.
- **Draw on Canvas**: Navigate to a page where you can draw directly on a canvas.

### Uploading an Image
1. Click on "Upload an Image".
2. Drag and drop an image or click the "Select a file..." button to upload.
3. The system processes the image and extracts the handwritten text.
4. The extracted text is displayed, and you can download the audio version.

### Drawing on Canvas
1. Click on "Draw on Canvas".
2. Use the drawing tools to write on the canvas.
3. Click "Upload" to process the handwritten content.
4. The system processes the canvas drawing and extracts the handwritten text.
5. The extracted text is displayed, and you can download the audio version.

## Implementation Details
- **Backend**: Implemented using Flask, a lightweight WSGI web application framework in Python.
- **Frontend**: Simple and responsive HTML/CSS with some JavaScript for canvas drawing.
- **OCR**: Utilizes Tesseract OCR for text recognition.
- **Audio Generation**: Converts recognized text into speech using Python libraries like `gTTS` (Google Text-to-Speech).

## Model Accuracy
NeuroScribe leverages Tesseract OCR, a highly accurate open-source OCR engine. The accuracy depends on the quality and clarity of the input handwriting. Well-formed and clearly written text yields the best results. The application is optimized for English language recognition.

## Contribution
We welcome contributions from the community to enhance NeuroScribe. Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

Thank you for using NeuroScribe. We hope this tool significantly enhances your productivity and experience with handwritten content!
