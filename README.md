# 🌱 CropDefender AI - Crop Disease Prediction & Management System

**CropDefender AI** is an AI-powered agricultural application that detects crop diseases from leaf images using **deep learning and computer vision**. The system analyzes uploaded plant images, identifies potential diseases, and provides **treatment and prevention recommendations** to help farmers protect crops and improve productivity.

---

## 🌟 Features

* **🤖 AI-Powered Disease Detection**
  Uses a deep learning-based image classification model to identify crop diseases from leaf images.

* **🌿 Crop Health Analysis**
  Analyzes plant foliage and determines whether the crop appears healthy or affected by disease.

* **📸 Image-Based Prediction**
  Upload a crop leaf image and receive an AI-generated disease prediction.

* **💊 Treatment Recommendations**
  Provides disease-specific treatment and preventive care suggestions based on the prediction.

* **⚡ Fast Prediction**
  Flask-based backend handles image processing and model inference through a REST API.

* **🖥️ Interactive Web Interface**
  User-friendly frontend designed to make crop disease detection simple and accessible.

* **📱 Responsive Design**
  Works across desktop and mobile screen sizes.

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Vite
* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask
* Flask-CORS
* REST API

### AI / Machine Learning

* TensorFlow
* Keras
* VGG19
* Convolutional Neural Networks (CNN)
* Image Classification

### Tools

* Git
* GitHub
* VS Code

---

## 🗂️ Project Structure

```text
CropDefender-AI/
│
├── app.py                         # Flask backend and API
│
├── models/
│   └── potato_disease_vgg19_model_3.h5
│                                  # Trained VGG19 disease classification model
│
├── frontend/
│   ├── public/
│   │   └── images/                # Frontend images and assets
│   │
│   ├── src/
│   │   ├── components/            # React components
│   │   ├── App.jsx                # Main React application
│   │   └── index.css              # Application styling
│   │
│   ├── package.json               # Frontend dependencies
│   └── vite.config.js             # Vite configuration
│
├── templates/                     # Flask/Jinja templates (if used)
│
├── static/                        # Static assets
│
├── requirements.txt               # Python dependencies
│
└── README.md                      # Project documentation
```

---

## 🚀 Getting Started

Follow these steps to run CropDefender AI locally.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/CropDefender-AI.git
cd CropDefender-AI
```

### 2. Set Up the Python Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, you can install the main dependencies with:

```bash
pip install flask flask-cors tensorflow keras opencv-python numpy pillow
```

### 4. Start the Flask Backend

```bash
python app.py
```

The backend will typically run at:

```text
http://localhost:5000
```

---

## 🎨 Running the React Frontend

Open a **new terminal** and navigate to the frontend directory:

```bash
cd frontend
```

Install the required Node.js packages:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will typically be available at:

```text
http://localhost:5173
```

Open the URL in your browser to use CropDefender AI.

---

## 🧠 How It Works

The application follows the following workflow:

```text
        Crop Leaf Image
               │
               ▼
        Image Preprocessing
               │
               ▼
        VGG19 CNN Model
               │
               ▼
       Disease Prediction
               │
               ▼
     Treatment Recommendation
               │
               ▼
          User Result
```

### Prediction Pipeline

1. User uploads a crop leaf image.
2. The image is sent to the Flask backend.
3. The backend preprocesses the image according to the model requirements.
4. The trained VGG19-based CNN analyzes the image.
5. The model predicts the crop disease/health condition.
6. The application displays the prediction.
7. Relevant treatment and preventive recommendations are provided.

---

## 🌾 Supported Crop Diseases

The current model focuses on **potato leaf disease classification**, including:

* 🥔 Potato Early Blight
* 🥔 Potato Late Blight
* 🌿 Healthy Potato Leaf

> The supported classes depend on the dataset and trained model included in the project.

---

## 🔮 Future Improvements

* Expand disease detection to additional crops.
* Add more plant disease classes.
* Improve model accuracy with larger and more diverse datasets.
* Add multilingual support for farmers.
* Integrate weather and environmental data.
* Add real-time mobile camera detection.
* Develop a dedicated Android application.
* Add disease history and prediction tracking.
* Deploy the complete application using cloud infrastructure.


## 👩‍💻 Author & Teamamte

**Ankita Yadav**
ML and Web Developer

**Himanshu**
ML and Deep Learning Developer

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!
