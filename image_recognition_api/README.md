# Image Recognition API

> This is a project to learn to build an API using an already-trained model for image recognition. I use FastAPI to build the API because it is the easiest option for this task. We use the MobileNetV2 model, trained with ImageNet from Keras. I use the PIL module and the Image class to preprocess the images. I basically create and endpoint with the API and make a simle interface with JS to make the user load an image, and the use that image, preprocess and use the model to predict the category of that image and return it in a text below the shown image. 

## Files

| Filename | Task |
| ------ | ------------------------------------------------- | 
| [prediction.py](https://github.com/otalorajuand/personal_projects/blob/main/image_recognition_api/prediction.py)| This file contains functions to load the trained model, to preprocess the images and to make predictions. | 
| [server.py](https://github.com/otalorajuand/personal_projects/blob/main/image_recognition_api/server.py)| This file creates the API and uses the functions from the prediction.py file to apply to an image that is loaded from the /api/predict endpoint. | 

## Demonstration GIF

![ezgif com-video-to-gif](https://github.com/otalorajuand/personal_projects/assets/22607461/08135286-a3e8-43a5-b577-c6312bd68336)

### Try It On Your Machine :computer:
```bash
git clone https://github.com/otalorajuand/personal_projects.git
cd image_recognition
pip install -r requirements.txt
python3 server.py
```
