from fastapi import FastAPI, UploadFile, File
import uvicorn
from prediction import read_imagefile, preprocess, predict
from starlette.responses import RedirectResponse


app = FastAPI()


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post('/api/predict')
async def predict_image(file: UploadFile = File(...)):
    # read the file uploaded by the user
    image = read_imagefile(await file.read())
    # preprocess the image
    image = preprocess(image)
    # make the prediction
    prediction = predict(image)
    print(prediction)
    return prediction


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")