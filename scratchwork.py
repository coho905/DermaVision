from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from fastai.vision.all import *
import pickle
import glob
import joblib
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


path = r'C:/Users/Coho9/Downloads/archive (5)/train'
benign_images = get_image_files(path + "benign")
malignant_images = get_image_files(path + "malignant")
len(malignant_images)
fnames = get_image_files(path)


def label_func(x): return x.parent.name


def load_model():
  path = r'C:/Users/Coho9/Downloads/model.pkl'
  learn = load_learner(path, 'model.pkl')
  return learn

path = r'C:/Users/Coho9/Downloads/model.pkl'
path = Path(path)
learn_inf = load_learner(path)
from PIL import Image
img = PILImage.create("1.jpg")
print(type(img))

img = load_image("1.jpg")
print(type(img))

print(learn_inf.predict(img))


