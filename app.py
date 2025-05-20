from io import BytesIO

from flask import Flask, render_template, request, send_file
from PIL import Image
from rembg import remove

app = Flask(__name__)


def process_file(file):
    in_img = Image.open(file.stream)
    out_img = remove(in_img, post_process_mask=True)
    img_io = BytesIO()
    out_img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io


OUTPUT_NAME = '_no_background_img.png'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if not file.filename:
            return 'No file selected', 400
        if file:
            processed_img = process_file(file)
            return send_file(processed_img, mimetype='image/png', as_attachment=True, download_name=OUTPUT_NAME)
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    if not file.filename:
        return 'No file selected', 400
    if file:
        processed_img = process_file(file)
        return send_file(processed_img, mimetype='image/png', as_attachment=True, download_name=OUTPUT_NAME)


@app.route('/health-test', methods=['GET'])
def test():
    return "I'm ok", 200
