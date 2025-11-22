from flask import Flask, render_template, request, url_for
from PIL import Image
import os
import random

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def process_image(image_path, key, encrypt=True):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()
    width, height = img.size

    random.seed(key)

    # Pixel manipulation
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if encrypt:
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
            else:
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    # Random pixel swap
    for _ in range(width * height // 10):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

    output_filename = 'processed_image.png'
    output_path = os.path.join('static', output_filename)
    img.save(output_path)
    return output_filename

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        key = request.form['key']
        action = request.form['action']

        if file and key.isdigit():
            key = int(key)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            encrypt = True if action == 'encrypt' else False
            processed_filename = process_image(filepath, key, encrypt)

            image_url = url_for('static', filename=processed_filename)
            return render_template('result.html', image_url=image_url)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
