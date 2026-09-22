# CropDefender AI - Crop Disease Prediction & Management System

CropDefender AI is an intelligent agricultural healthcare application that diagnoses crop foliage diseases in real time using deep learning (VGG19 Convolutional Neural Networks) and provides actionable treatment plans to protect crops and optimize yields.

---

## 🌟 Features

- **Modern React Frontend**: Clean, responsive UI with agriculture-themed aesthetics, glassmorphism cards, and mobile-ready navigation.
- **Dual Capture Methods**: Upload high-res images from your device or use the live webcam feed with one-click snapshot capture.
- **Deep Learning Disease Detection**: Powered by a VGG19 CNN model capable of identifying Potato Early Blight, Late Blight, and general leaf health status.
- **Instant Treatment Advisory**: Delivers customized agronomic treatments and preventative care instructions based on the detected condition.
- **Vercel-Ready**: Pre-configured for deployment on Vercel with single-page app routing.

---

## 🛠️ Project Structure

```
CropDefenderAI-Final/
├── app.py                      # Flask REST API + Legacy template routes
├── models/
│   └── potato_disease_vgg19_model_3.h5 # Trained VGG19 model (~157MB)
├── frontend/                   # Modern React (Vite) frontend
│   ├── public/images/          # Assets and images
│   ├── src/
│   │   ├── components/         # Header, Footer, Webcam, CropCards, Team, Prediction
│   │   ├── App.jsx             # Main application orchestrator
│   │   └── index.css           # Premium responsive styling
│   ├── vercel.json             # Vercel SPA routing configuration
│   └── package.json            # Node dependencies and build scripts
├── templates/                  # Original Jinja2 HTML templates
└── static/                     # Original static assets
```

---

## 🚀 Getting Started (Local Development)

### 1. Start the Flask Backend
Make sure you have Python 3.10+ installed with required libraries:
```bash
pip install flask flask-cors opencv-python tensorflow keras
python app.py
```
The Flask API will start running at `http://localhost:5000`.

### 2. Start the React Frontend
In a new terminal window:
```bash
cd frontend
npm install
npm run dev
```
Open your browser at `http://localhost:5173` to explore the application!

---

## 🌐 Deploying Frontend to Vercel

1. Push this repository to **GitHub / GitLab / Bitbucket**.
2. Go to [Vercel Dashboard](https://vercel.com/dashboard) and click **"Add New Project"**.
3. Import your GitHub repository.
4. In the **Project Configuration** settings:
   - **Root Directory**: Set to `frontend`
   - **Framework Preset**: `Vite`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
5. *(Optional)* Under **Environment Variables**, add:
   - `VITE_API_URL`: URL of your deployed Flask backend (e.g. `https://your-cropdefender-api.onrender.com`).
6. Click **Deploy**!

---

## 👥 Authors & Team
- **Himanshu** - Machine & Deep Learning | UI & UX Designer | Web Developer
- **Ankita Yadav** - Machine Learning & Web Designer
- **Dr. Prakash Singh** - AI & ML Expert | HOD CSE Department
