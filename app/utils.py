import numpy as np
from tensorflow.keras.models import load_model as keras_load_model
from PIL import Image

def load_model(path):
    return keras_load_model(path, compile=False)

def preprocess(image):
    image = image.convert('RGB')
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def predict(model, input_tensor):
    pred = model.predict(input_tensor, verbose=0)
    predicted_class_index = np.argmax(pred)
    labels = ['Mild Impairment', 'Moderate Impairment', 'No Impairment', 'Very Mild Impairment']
    predicted_label = labels[predicted_class_index]
    return predicted_label, round(pred.max()*100,2)
