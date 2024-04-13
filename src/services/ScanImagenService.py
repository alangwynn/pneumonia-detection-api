from src.utils.Logger import Logger
import tensorflow as tf
from keras.preprocessing import image
import numpy as np

class ScanImageService():

    @classmethod
    def image_prediction(cls, image_path):
        test_image = image.load_img(image_path, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0
        
        model_path = "data/models/pneumonia_detection_model.h5"
        
        model_loaded = tf.keras.models.load_model(model_path)
        
        prediction = model_loaded.predict(test_image)
        
        if prediction[0] > 0.5:
            statistic = prediction[0] * 100 
            return statistic, "PNEUMONIA"
        else:
            statistic = (1.0 - prediction[0]) * 100
            return statistic, "NORMAL"
