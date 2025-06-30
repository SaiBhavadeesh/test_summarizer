from fastapi import FastAPI
import uvicorn
import os, sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response

from src.text_summarizer.pipeline.prediction import PredictionPipeline

text: str = "What is text summarization?"

app = FastAPI()


@app.get("/", tags=["authentication"])
async def index():
    """
    Redirects to the /docs endpoint.
    """
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train():
    """
    Endpoint to trigger the training process.
    """
    try:
        os.system("python main.py")
        return Response("Training successfull !!")
    except Exception as e:
        return Response(f"Error occured ! {e}")


@app.post("/predict")
async def predict(text: str):
    """
    Endpoint to get the summary of the text.
    """
    try:
        prediction_pipeline = PredictionPipeline()
        summary = prediction_pipeline.predict(text)
        return {"summary": summary}
    except Exception as e:
        return Response(f"Error occured ! {e}")


if __name__ == "__main__":
    """
    Run the FastAPI application.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
