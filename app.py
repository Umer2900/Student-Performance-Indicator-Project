from flask import Flask, request, render_template
import numpy as np
import pandas as pd
    
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

## Route for home page
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    try:
        if request.method == 'GET':
            return render_template('home.html')

        # Get form data
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        # Check for missing values
        if None in [data.gender, data.race_ethnicity, data.parental_level_of_education,
                    data.lunch, data.test_preparation_course]:
            return "Error: Please fill all the fields!"

        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=float(results[0]))

    except Exception as e:
        print("ERROR:", e)
        return f"Error occurred: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
