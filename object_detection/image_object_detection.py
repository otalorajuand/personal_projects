import cv2

img = cv2.imread('juan.png')

# Load the class names from a file
classNames = []
classFile = "model/coco_names.txt"
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')


# Load the pre-trained model
configPath = 'model/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'model/frozen_inference_graph.pb'
net = cv2.dnn_DetectionModel(weightsPath, configPath)

# Set the input size, scale, mean, and swap RB channels for the model
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


# Detect objects in the frame using the pre-trained model
classIds, confs, bbox = net.detect(img, confThreshold=0.6)

# Check if any objects are detected
if len(classIds) != 0:
    # Iterate over each detected object
    for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
        # Draw a rectangle around the object on the image
        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)

        # Add a text label to the object indicating its class name
        cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    

# Show the output image with detections
cv2.imshow("output", img)
cv2.waitKey(0)

