# 🌫️ AQI Predictor Web App

A Machine Learning-based web application that predicts the **Air Quality Index (AQI)** based on various environmental pollutants and provides health recommendations.

---

## 🚀 Project Overview

The **AQI Predictor** is an end-to-end ML project that:

* Takes real-world air pollutant data as input
* Uses a trained Machine Learning model to predict AQI
* Categorizes air quality levels
* Provides health advice based on predicted AQI

This project demonstrates the complete ML pipeline from **data preprocessing → model training → deployment**.

---

## 🎯 Features

* 📊 Predict AQI based on pollutant levels
* 🌆 City-wise prediction using encoded features
* 📅 Date-based feature extraction (year, month, day)
* 🎨 Color-coded AQI categories
* 🩺 Health recommendations based on AQI levels
* ⚡ Interactive UI using Streamlit
* ☁️ Cloud deployment (Railway)

---

## 🧠 Machine Learning Workflow

1. **Data Collection**

   * Dataset: `city_day.csv`
   * Contains pollutant levels and AQI values

2. **Data Preprocessing**

   * Handling missing values
   * Date feature extraction (year, month, day)
   * One-hot encoding for cities
   * Feature scaling using StandardScaler

3. **Model Training**

   * Algorithm: Random Forest Regressor
   * Hyperparameters:

     * `n_estimators = 10`
     * `max_depth = 8`
   * Evaluation metrics:

     * RMSE (Root Mean Squared Error)
     * R² Score

4. **Model Saving**

   * Saved as:

     * `model.pkl`
     * `scaler.pkl`
     * `columns.pkl`

---

## 🛠️ Tech Stack

| Category        | Technology Used |
| --------------- | --------------- |
| Language        | Python          |
| ML Library      | scikit-learn    |
| Data Handling   | pandas, numpy   |
| Visualization   | Streamlit       |
| Version Control | Git & GitHub    |

---

## 📂 Project Structure

```
ML_Project/
│── app.py                # Streamlit web app
│── train.py              # Model training script
│── requirements.txt      # Dependencies
│── runtime.txt           # Python version
│
├── data/
│   └── city_day.csv
│
├── model/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
└── notebook/
    └── aqi_notebook.ipynb
```

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AQI_predictor.git
cd AQI_predictor
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Train Model (if needed)

```bash
python train.py
```

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

```

---

## 📊 AQI Categories

| AQI Range | Category     |
| --------- | ------------ |
| 0–50      | Good         |
| 51–100    | Satisfactory |
| 101–200   | Moderate     |
| 201–300   | Poor         |
| 301–400   | Very Poor    |
| 401+      | Severe       |

---

## ⚠️ Challenges Faced

* Version mismatch between sklearn and pandas
* Deployment issues (port binding & caching)
* Git tracking issues for model files

---

## 🔮 Future Improvements

* Add real-time AQI API integration
* Improve model accuracy
* Add visual charts & analytics
* Deploy using Docker for scalability

---

---

## ⭐ Acknowledgements

* scikit-learn documentation
* Streamlit documentation
* Open AQI datasets

---

## 📌 Conclusion

This project showcases how Machine Learning can be used to solve real-world environmental problems by predicting air quality and helping users make informed decisions.

---
