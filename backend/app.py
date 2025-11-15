import os
import json
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# FIXED PATHS
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model_final.h5")
LABELS_PATH = os.path.join(BASE_DIR, "models", "labels.json")

print("Model path = ", MODEL_PATH)
print("Labels path = ", LABELS_PATH)

model = load_model(MODEL_PATH)

# Load labels
with open(LABELS_PATH, "r") as f:
    label_map = json.load(f)

label_map = {int(k): v for k, v in label_map.items()}

IMG_SIZE = (224, 224)


def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize(IMG_SIZE)

    arr = img_to_array(img)
    arr = preprocess_input(arr)   # << MobileNetV2 preprocessing
    arr = np.expand_dims(arr, axis=0)

    return arr


@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    img_bytes = file.read()

    img_arr = preprocess_image(img_bytes)
    preds = model.predict(img_arr)
    idx = int(np.argmax(preds))
    conf = float(np.max(preds))

    return jsonify({
        "label": label_map[idx],
        "confidence": conf
    })


@app.route('/')
def home():
    return "Crop Disease Detection Backend Running"


if __name__ == "__main__":
    app.run(debug=True)
