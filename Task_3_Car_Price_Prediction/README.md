# 🚗 Car Price Predictor

A modern Machine Learning web application that predicts the selling price of used cars based on various vehicle attributes.

Developed as part of the **Oasis Infobyte Data Science Internship (OIBSIP)**.

---

# Features

* Modern responsive UI
* Dark themed professional interface
* Machine Learning based price prediction
* Flask backend
* Random Forest Regressor model
* Real-time prediction results
* Mobile friendly design

---

# Tech Stack

### Frontend

* HTML5
* CSS3

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

---

# Project Structure

```
Task_3_Car_Price_Prediction
│
├── app.py
├── car_price_model.pkl
├── Dataset.csv
├── requirements.txt
├── README.md
├── Task_3_Car_Price_Prediction.ipynb
│
├── static
│   └── style.css
│
├── templates
│   ├── index.html
│   └── result.html
│
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/BhvyaVaish/OIBSIP.git
```

Move inside project

```bash
cd Task_3_Car_Price_Prediction
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# Machine Learning Model

Model Used

* Random Forest Regressor

Input Features

* Present Price
* Driven Kilometers
* Number of Previous Owners
* Fuel Type
* Seller Type
* Transmission Type

Output

Predicted Selling Price

---

# Internship

This project was developed for

**Oasis Infobyte Data Science Internship (OIBSIP)**

---

# Author

**Bhvya Vaish**

GitHub

https://github.com/BhvyaVaish
