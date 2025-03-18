# Import required libraries
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import io

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained ResNet50 model (ImageNet weights)
model = ResNet50(weights='imagenet')

@app.get("/")
async def root():
    # Root endpoint to verify API is running
    return {"status": "ML API Server (TensorFlow) is running."}

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    # Read the uploaded image
    image_data = await image.read()

    # Convert image to RGB explicitly to handle PNG (RGBA) images
    img = Image.open(io.BytesIO(image_data)).convert('RGB')
    # Open and resize the image to 224x224 pixels (required input size for ResNet50)
    img = img.resize((224, 224))
    

    # Convert image to numpy array and preprocess for model input
    img_array = np.array(img)[np.newaxis, ...]
    img_processed = preprocess_input(img_array)

    # Generate predictions using the pre-trained model
    predictions = model.predict(img_processed)

    # Decode predictions into human-readable labels
    results = decode_predictions(predictions, top=3)[0]

    # Format predictions into JSON-friendly structure
    predictions_json = [
        {"label": res[1], "confidence": float(res[2])} for res in results
    ]

    # Return predictions as JSON
    return JSONResponse(content={"predictions": predictions_json})
