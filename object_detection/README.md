# Object Detection

> In this project I used the MobileNet V3 pre-trained model from OpenCV and apply it for object detection. There are two modalities for this code, you can use it on an image or with the camera of your computer. This code will put a green rectangle in the object and a word with the prediction of the model. The object of this project is to learn how to implement this kind of model and explore its possibilities.

## Usage

There are two files to be executed: main.py which is executed to predict object detection based on the video from the web camera from your computer and image_object_detection.py to predict object detection based on an image in the current directory.

## Files

| Filename | Description |
| ------ | ------------------------------------------------- | 
| [main.py](https://github.com/otalorajuand/personal_projects/blob/main/object_detection/main.py)| This is the main file and the file to be executed for object detection with the webcam of your computer |
| [image_object_detection.py](https://github.com/otalorajuand/personal_projects/blob/main/object_detection/image_object_detection.py)| This file predict object detection based on an image. |
| [frozen_inference_graph.pb](https://github.com/otalorajuand/personal_projects/blob/main/object_detection/frozen_inference_graph.pb)| This is the weights and graph of the model. | 
| [coco_names.txt](https://github.com/otalorajuand/personal_projects/blob/main/object_detection/coco_names.txt)| The names of the categories predicted. | 
| [ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt](https://github.com/otalorajuand/personal_projects/blob/main/object_detection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt)| This file contains the configuration of the model. | 


## Demonstration GIF

### Image Object Detection
<img width="637" alt="image" src="https://github.com/otalorajuand/personal_projects/assets/22607461/f1057994-40d1-4c0f-8a1c-c52e969b75f1">


### Video Object Detection

![ezgif com-gif-to-mp4](https://github.com/otalorajuand/personal_projects/assets/22607461/73273e65-e964-46bd-aa52-08500515671a)


### Try It On Your Machine :computer:
```bash
git clone https://github.com/otalorajuand/personal_projects.git
cd object_detection
pip install -r requirements.txt
python3 main.py
```
