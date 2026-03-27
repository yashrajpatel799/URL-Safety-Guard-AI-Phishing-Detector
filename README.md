# 🛡️ PhishShield: AI-Powered URL Safety Detection System

🚀 Live Demo: https://url-safety-guard-ai-phishing-detector-1.onrender.com/  
📂 GitHub Repository: https://github.com/yashrajpatel799/URL-Safety-Guard-AI-Phishing-Detector  

---

## 📌 Overview

PhishShield is a **Machine Learning-based web application** that detects whether a given URL is **safe or phishing**.  
It uses Natural Language Processing (NLP) techniques and a Logistic Regression model to classify URLs in real-time.

---

## ✨ Features

- 🔍 Real-time URL analysis  
- 🤖 Machine Learning-based prediction  
- 📊 TF-IDF vectorization for text processing  
- 🧠 Logistic Regression model  
- 🕒 Recent search history tracking  
- 🌐 Simple and interactive web interface  

---

## 🧠 Tech Stack

- **Frontend:** HTML, CSS  
- **Backend:** Flask  
- **Machine Learning:** Scikit-learn  
- **NLP:** TF-IDF Vectorizer  
- **Deployment:** Render  

---

## ⚙️ How It Works

1. User enters a URL  
2. URL is cleaned and preprocessed  
3. TF-IDF Vectorizer converts text → numerical features  
4. Logistic Regression model predicts:
   - ✅ Safe URL  
   - ⚠️ Phishing URL  
5. Result is displayed instantly  

---

## 📂 Project Structure


/my_ml_app
│── app.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── Procfile
├── templates/
│ └── index.html


---

## 🚀 Installation (Run Locally)

```bash
git clone https://github.com/yashrajpatel799/URL-Safety-Guard-AI-Phishing-Detector.git
cd URL-Safety-Guard-AI-Phishing-Detector
pip install -r requirements.txt
python app.py

🌐 Deployment:

This project is deployed on Render:
👉 https://url-safety-guard-ai-phishing-detector-1.onrender.com/

📊 Model Details:

Algorithm: Logistic Regression
Feature Extraction: TF-IDF Vectorization
Input: URL text
Output: Classification (Safe / Phishing)


🎯 Future Improvements:

🔐 Add HTTPS certificate validation
📈 Show prediction confidence score
🧩 Use advanced models (Random Forest / XGBoost)
🎨 Improve UI with modern frameworks
☁️ Add database for persistent history

👨‍💻 Author
Yash Raj Patel
📌 B.Tech CSE Student
