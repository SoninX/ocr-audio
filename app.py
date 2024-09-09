from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(filename):
    # Placeholder for OCR processing
    ocr_text = "Recognized text from the image would be displayed here."
    # Placeholder for audio processing
    audio_filename = 'sample_audio.mp3'
    return ocr_text, audio_filename

@app.route("/")
def index():
    return render_template('upload.html')

@app.route("/upload", methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        ocr_text, audio_filename = process_image(filename)
        
        return redirect(url_for('uploaded_file', filename=filename, ocr_text=ocr_text, audio_filename=audio_filename))
    return redirect(request.url)

@app.route("/upload/<filename>")
def uploaded_file(filename):
    ocr_text = request.args.get('ocr_text', 'OCR text not available')
    audio_filename = request.args.get('audio_filename', 'audio_file_not_available.mp3')
    return render_template('result.html', filename=filename, ocr_text=ocr_text, audio_filename=audio_filename)

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
