# image_prediction_app/predict.py
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from io import BytesIO
from .models import PredictedImage

def predict_and_save_image(uploaded_file):
    model = tf.keras.applications.ResNet50(weights='imagenet')

    # Read the uploaded file as bytes
    file_bytes = BytesIO(uploaded_file.read())

    # Load the image using Keras image module
    img = image.load_img(file_bytes, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make a prediction
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0]
    predicted_label = decoded_predictions[0][1]

    # Save the predicted image and result to the database
    predicted_image = PredictedImage(prediction=predicted_label, image=uploaded_file)
    predicted_image.save()

    return predicted_label
