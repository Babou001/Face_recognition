from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from search import inference, get_model
import os
import pandas as pd
from dataset import get_data
from image_search  import search_face
from werkzeug.utils import secure_filename

app = Flask(__name__)

model = get_model()

data = get_data()

current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir, 'data.csv')
images_dir = os.path.join(current_dir, 'images')
app.config['UPLOAD_FOLDER'] = images_dir

@app.route('/recherche', methods=['GET'])
def search():
    search_description = request.args.get('search_description')
    search_image = request.files.get('search_image')  # Pour l'instant non utilisé

    results = {}
    if search_description:
        results = inference(search_description, model)

    if search_image:
        image_filename = secure_filename(search_image.filename)
        image_path = os.path.join('static', 'uploads', image_filename)
        search_image.save(image_path)
        
        # Recherche d'image dans le dataset
        results = search_face(image_path)
    return render_template('recherche.html', results=results)

@app.route('/librairie', methods=['GET'])
def librairie():
    df = pd.read_csv(data_file)
    images = df['Chemin_d_acces'].tolist()
    descriptions = df['Description'].tolist()
    return render_template('librairie.html', images=images, descriptions=descriptions, zip=zip)

@app.route('/ajouter_image', methods=['GET', 'POST'])
def ajouter_image():
    if request.method == 'POST':
        image_file = request.files['image']
        description = request.form['description']

        if image_file:
            df = pd.read_csv(data_file) 
            if df.empty:
                image_id = 1
            else:
                image_id = int(df['Index'].max()) + 1
            image_filename = f"image{image_id+1}.jpg"
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            image_file.save(image_path)
            relative_image_path = os.path.join('images', image_filename)
            new_entry = pd.DataFrame([[image_id, relative_image_path, description]], columns=['Index', 'Chemin_d_acces', 'Description'])
            df = pd.concat([df, new_entry], ignore_index=True)

            df.to_csv(data_file, index=False)

            return redirect(url_for('librairie'))

    return render_template('ajouter_image.html')


@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(images_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
