Dataset link :

https://drive.google.com/file/d/1abdLSupYQAH_YO2PQF-9wfQ7JB3Pz_51/view?usp=drive_link

🌱 Crop Disease Prediction System

A machine learning–powered system that predicts plant leaf diseases from images with high accuracy.
The system processes an uploaded leaf image, classifies the disease using a trained CNN model, and provides confidence scores along with suggested remedies.
It is designed to assist farmers, agriculture researchers, and precision-farming applications.
______________________________________________________________________

🤖 Model Details

Model Type: Convolutional Neural Network (CNN)
Input Size: 224 × 224 × 3
Activation Functions: ReLU, Softmax
Optimizer: Adam
Loss Function: Sparse Categorical Crossentropy
Epochs: 30
Batch Size: 32
Accuracy Achieved: ~98–99% during validation
_____________________________________________________________
✨ Key Features

📸 Predicts crop diseases from leaf images using a CNN model
🎯 High-accuracy classification across multiple crop species
📊 Displays prediction probability and model confidence
💡 Provides suggested remedies and preventive measures
⚡ Works efficiently on CPU (no GPU required)
🌾 Supports multiple crop categories and diseases
🔌 Easy REST API integration for frontend applications

___________________________________________________________-
🧠 Tech Stack

Model: TensorFlow, Keras (Custom CNN model)
Backend: Python (FastAPI)
Frontend: (React or any simple interface consuming API)
Deployment: Local machine / Server
Dataset: PlantVillage (or your curated dataset)
___________________________________________________________

📂 Project Structure
crop-disease-prediction-system/
│── backend/
│   ├── main.py
│   ├── model/
│   │   └── saved_model/
│   ├── utils/
│   │   └── preprocess.py
│   └── requirements.txt
│
│── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
│── trained_model/
│── README.md
_____________________________________________________

Contributors
Anushka Gurav
Tasnim Shaikh
Shivani Ippar
Sana Khan

________________________________________________
