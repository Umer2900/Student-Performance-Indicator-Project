from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = FastAPI(title="Student Performance Indicator")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
@app.post("/", response_class=HTMLResponse)
async def home(
    request: Request,
    gender: str = Form(None),
    race_ethnicity: str = Form(None),
    parental_level_of_education: str = Form(None),
    lunch: str = Form(None),
    test_preparation_course: str = Form(None),
    reading_score: float = Form(None),
    writing_score: float = Form(None),
):
    results = None
    form_data = None
    error = None

    if request.method == "POST":
        try:
            # Validate that all fields are provided on POST
            if None in [
                gender,
                race_ethnicity,
                parental_level_of_education,
                lunch,
                test_preparation_course,
                reading_score,
                writing_score,
            ]:
                raise ValueError("All fields are required.")

            data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score,
            )

            pred_df = data.get_data_as_data_frame()
            predict_pipeline = PredictPipeline()
            predictions = predict_pipeline.predict(pred_df)

            results = round(float(predictions[0]), 2)

            # Keep form data to repopulate fields
            form_data = {
                "gender": gender,
                "race_ethnicity": race_ethnicity,
                "parental_level_of_education": parental_level_of_education,
                "lunch": lunch,
                "test_preparation_course": test_preparation_course,
                "reading_score": reading_score,
                "writing_score": writing_score,
            }

        except Exception as e:
            error = f"Error: {str(e)}"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "results": results,
            "form_data": form_data,
            "error": error,
        },
    )


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)


# RUN: uvicorn app:app --reload --port 8000
