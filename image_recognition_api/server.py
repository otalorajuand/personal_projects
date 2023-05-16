from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from prediction import read_imagefile, preprocess, predict
from starlette.responses import RedirectResponse


app = FastAPI()

# CORS adjustment
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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