import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import img_to_array
from fastapi import FastAPI, UploadFile, File, HTTPException
import numpy as np
from io import BytesIO
from PIL import Image

app = FastAPI()

# Load the trained model
cnn_model = tf.keras.models.load_model('cnn_model')

# Class labels for CIFAR-10
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

def preprocess_image(image_bytes):
    """Preprocesses the image for prediction."""
    try:
        img = Image.open(BytesIO(image_bytes)).resize((32, 32)) # resize
        img_array = img_to_array(img) / 255.0 # normalize
        img_array = np.expand_dims(img_array, axis=0) # add batch dimension
        return img_array
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")

@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    """Predicts the class of an uploaded image."""
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File is not an image.")

    image_bytes = await file.read()
    processed_image = preprocess_image(image_bytes)

    prediction = cnn_model.predict(processed_image)
    predicted_class_index = np.argmax(prediction)
    predicted_class_name = class_names[predicted_class_index]
    confidence = prediction[0][predicted_class_index]

    return {"prediction": f"<h2>Predicted class: {predicted_class_name}, Confidence: {confidence:.4f}</h2>"}