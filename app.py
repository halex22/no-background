from io import BytesIO

from flask import Flask, render_template, request, send_file
from PIL import Image
from rembg import remove

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print('post received')
        if 'file' not in request.files:
            return 'No file uploaded', 400
        ...
    
    return render_template('index.html')

@app.route('/another-test')
def test():
    return "another test three"