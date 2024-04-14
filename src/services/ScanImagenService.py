import os

from src.utils.Logger import Logger
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from PIL import Image
from io import BytesIO

def convert_grayscale_to_rgb(image):
    if image.mode == 'RGB':
        return image
    return image.convert('RGB')

class ScanImageService():

    @classmethod
    def image_prediction(cls, image_data):
        img = Image.open(image_data)
        img_resized = img.resize((224, 224))
        img_rgb = convert_grayscale_to_rgb(img_resized)
        test_image = image.img_to_array(img_rgb)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0
        
        model_filename = "pneumonia_detection_model.h5"
        model_path = os.path.join("src", "data", "models", model_filename)
        
        model_loaded = tf.keras.models.load_model(model_path)
        
        prediction = model_loaded.predict(test_image)
        
        if prediction[0] > 0.5:
            statistic = prediction[0] * 100 
            prediction_float = float(statistic)
            return prediction_float, "Paciente con neumonía", "Proceder con los estudios pos análisis"
        else:
            statistic = (1.0 - prediction[0]) * 100
            prediction_float = float(statistic)
            return prediction_float, "Paciente sin neumonía", ""
