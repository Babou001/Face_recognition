from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)

images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

@app.route('/librairie')
def index():
    image_files = [f for f in os.listdir(images_dir) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    return render_template('librairie.html', images=image_files)

@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(images_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
