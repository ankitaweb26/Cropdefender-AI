from flask import Flask, render_template, request, send_from_directory, jsonify
from flask_cors import CORS
import cv2
import pickle
import joblib
import numpy as np
from keras.models import load_model
import os

# Load model
model_potato = load_model("./models/potato_disease_vgg19_model_3.h5")

COUNT = 0
app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend requests
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1

# Ensure static img directory exists
os.makedirs('static/img', exist_ok=True)

def process_potato_image(image_bytes_or_file):
    # Read image from memory or path
    file_bytes = np.frombuffer(image_bytes_or_file.read(), np.uint8)
    img_arr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    if img_arr is None:
        return "Invalid image", "Could not decode the uploaded image. Please provide a valid image file."

    # Save to disk for legacy template support
    global COUNT
    cv2.imwrite('static/img/{}.jpg'.format(COUNT), img_arr)

    # Preprocess
    img_resized = cv2.resize(img_arr, (224, 224))
    img_normalized = img_resized / 255.0
    img_reshaped = img_normalized.reshape(1, 224, 224, 3)

    predictions = model_potato.predict(img_reshaped)
    confidence = float(np.max(predictions))
    prediction = int(np.argmax(predictions, axis=1)[0])

    threshold = 0.1
    if confidence < threshold:
        return "Invalid image", "Please upload a clear image of a potato leaf."

    COUNT += 1

    if prediction == 0:
        return "Potato_Early_blight", "Balanced Fertilization: Ensure proper levels of nitrogen, potassium, and phosphorus in the soil. Excess nitrogen can increase plant susceptibility, while adequate potassium can improve plant resistance."
    elif prediction == 1:
        return "Potato_Late_blight", "Ensure adequate spacing between plants to promote air circulation and reduce humidity, which favors blight development. Apply appropriate fungicides if necessary."
    elif prediction == 2:
        return "Potato_healthy", "Healthy Plant. Maintain current watering, soil nutrients, and sunlight conditions."
    else:
        return "Not a Potato Image", "Please upload a clear image of a potato leaf."

# --- API Endpoints for React Frontend ---

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "CropDefender AI Backend is running"})

@app.route('/api/predict/potato', methods=['POST'])
def api_predict_potato():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided in request."}), 400

    img = request.files['image']
    if img.filename == '':
        return jsonify({"error": "No image selected."}), 400

    disease, treatment = process_potato_image(img)
    return jsonify({
        "status": "success",
        "disease": disease,
        "treatment": treatment
    })

# --- Legacy Template Routes ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inputpotato')
def inputpotato():
    return render_template('prediction_potato.html')

@app.route('/predictionpotato', methods=['POST'])
def predictionpotato():
    if 'image' not in request.files:
        return render_template('Output.html', data=["Invalid image", "No image uploaded."])
    
    img = request.files['image']
    disease, treatment = process_potato_image(img)
    return render_template('Output.html', data=[disease, treatment])

@app.route('/load_img')
def load_img():
    global COUNT
    return send_from_directory('static/img', "{}.jpg".format(max(0, COUNT - 1)))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
