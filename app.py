from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
import pytesseract
from PIL import Image
import pyttsx3
import base64
import io
import time

app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set the Tesseract executable path if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(filename):
    # Perform OCR using Tesseract
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image = Image.open(image_path)
    ocr_text = pytesseract.image_to_string(image)

    # Generate audio using pyttsx3
    engine = pyttsx3.init()
    audio_filename = os.path.splitext(filename)[0] + '.mp3'
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)
    engine.save_to_file(ocr_text, audio_path)
    engine.runAndWait()

    return ocr_text, audio_filename

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload_file", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
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
    return render_template('upload_file.html')

@app.route("/upload_canvas", methods=['GET'])
def upload_canvas_get():
    return render_template('upload_canvas.html')

@app.route("/upload_canvas", methods=['POST'])
def upload_canvas_post():
    if 'canvas_image' not in request.form:
        return redirect(request.url)
    image_data = request.form['canvas_image']
    image_data = image_data.split(",")[1]
    image_data = base64.b64decode(image_data)
    filename = secure_filename(f"uploaded_canvas_{int(time.time())}.png")
    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "wb") as f:
        f.write(image_data)
    ocr_text, audio_filename = process_image(filename)
    return redirect(url_for('uploaded_file', filename=filename, ocr_text=ocr_text, audio_filename=audio_filename))

@app.route("/upload/<filename>")
def uploaded_file(filename):
    ocr_text = request.args.get('ocr_text', 'OCR text not available')
    audio_filename = request.args.get('audio_filename', 'audio_file_not_available.mp3')
    return render_template('result.html', filename=filename, ocr_text=ocr_text, audio_filename=audio_filename)

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
