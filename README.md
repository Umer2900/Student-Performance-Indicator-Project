# 🎓 Student Performance Indicator  
### 🏆 Best Model: **Ridge Regression** | **R² Score: 0.880593**

> **Predicting student academic performance using Machine Learning**

A complete **end-to-end Machine Learning project** that predicts a student’s **Maths score** based on demographic and academic attributes.  
The project includes **Exploratory Data Analysis (EDA), model training, preprocessing pipelines, and a Flask-based web application** for real-time predictions.

---

## 🎥 Demo

![App Demo](assets/demo.gif)

---

## 🚀 Features

- 📊 **Exploratory Data Analysis (EDA):** In-depth analysis of factors affecting student scores.
- 🧠 **Machine Learning Training:** Comparison of multiple regression models to find the best fit.
- ⚙️ **Data Preprocessing:** Robust automated pipelines for handling categorical and numerical data.
- 🌐 **Flask Web App:** Interactive web interface for real-time score prediction.
- 🎨 **Modern UI:** Clean and user-friendly design.
- 📦 **Modular Structure:** Clean, scalable, and professional code organization.
- 🔐 **Robust Error Handling:** Custom exception handling and detailed logging for debugging.

---

## 🛠️ Tech Stack

### **Programming & ML**
- **Python**: Core programming language.
- **NumPy & Pandas**: Data manipulation and cleaning.
- **Scikit-learn**: Model training and preprocessing.
- **CatBoost**: Advanced gradient boosting library.

### **Web Framework**
- **Flask**: Lightweight web framework for the backend.
- **HTML5 / CSS3**: Frontend structure and styling.

### **Tools**
- **Jupyter Notebook**: For experimentation and EDA.
- **Git & GitHub**: Version control.

---

## 📁 Project Structure

```text
Student-Performance-Project/
├── notebook/                   # Jupyter notebooks
│   ├── data/
│   │   └── stud.csv            # Dataset
│   ├── EDA.ipynb               # Exploratory Data Analysis
│   └── Model_Training.ipynb    # Model training & evaluation
│
├── src/                        # Source code
│   ├── components/             # Data ingestion, transformation, model trainer
│   ├── pipeline/               # Training & Prediction pipelines
│   │   └── predict_pipeline.py 
│   ├── utils.py                # Utility functions
│   ├── logger.py               # Logging configuration
│   └── exception.py            # Custom exception handling
│
├── templates/                  # HTML templates
│   └── index.html              # Frontend UI
│
├── app.py                      # Flask application entry point
├── requirements.txt            # Python dependencies
├── setup.py                    # Project setup file
└── README.md                   # Project documentation