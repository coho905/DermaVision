from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from fastai.vision.all import *
import pickle
import glob
import joblib
import os
import uuid
import flask
import urllib
from PIL import Image
app = Flask(__name__)
from flask import Flask, render_template, request, session
import os
from werkzeug.utils import secure_filename
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


path = r'PATH to the folder with your images'
benign_images = get_image_files(path + "benign")
malignant_images = get_image_files(path + "malignant")
len(malignant_images)
fnames = get_image_files(path)


def label_func(x): return x.parent.name

path = r'path to model'
path = Path(path)
learn_inf = load_learner(path)

# WSGI Application
# Defining upload folder path
#UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name for template path
# The default folder name for static files should be "static" else need to mention custom folder for static path
# Configure upload folder for Flask application
app.config['UPLOAD_FOLDER'] = r'path to upload photo'


# Define secret key to enable session
app.secret_key = 'This is your secret key to utilize session in Flask'
prediction = ''
con_level = ''
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        # Unpickle classifier
        # Get values through input bars
        uploaded_img = request.files['weight1']
        # Extracting uploaded data file name
        img_filename = secure_filename(uploaded_img.filename)
        # Upload file to database (defined uploaded folder in static path)
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        # Storing uploaded file path in flask session
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
        img_file_path = session.get('uploaded_img_file_path', None)
        print(img_file_path)
        img = Image.open(img_file_path)
        img = PILImage.create(img_file_path)
        img = load_image(img_file_path)
        pred,prob,prob = learn_inf.predict(img)
        prob1 = prob[0]
        prob2 = prob[1]
        prob3 = 0
        if prob1> prob2:
            prob3 = prob1
        else:
            prob3 = prob2
        prob3 = prob3*100
        prob3 = str(prob3)
        prob3 = prob3.replace("TensorBase(", "")
        prob3 = prob3.replace(")", "")
        con_level = prob3
        prediction = pred
    else:
        prediction = ""
        con_level = ''
        img_file_path=''

    return render_template('index.html', msg=prediction, msg1=con_level)




if __name__ == '__main__':
    app.run(debug=True)
