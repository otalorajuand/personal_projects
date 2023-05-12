from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow.keras as K


def load_model():
    model = K.applications.MobileNetV2(weights="imagenet")
    return model

_model = load_model()

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

def preprocess(image: Image.Image):

    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0

    return image


def predict(image: Image.Image):
    prediction = _model.predict(image)
    prediction = K.applications.imagenet_utils.decode_predictions(prediction)[0][0][1]
    return prediction

