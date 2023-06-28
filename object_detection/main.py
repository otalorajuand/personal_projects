import cv2

#img = cv2.imread('juan.png')

# Open the webcam for video capture
cap = cv2.VideoCapture(0)

# Set the resolution of the captured video
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Load the class names from a file
classNames = []
classFile = "coco_names.txt"
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')


# Load the pre-trained model
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'
net = cv2.dnn_DetectionModel(weightsPath, configPath)

# Set the input size, scale, mean, and swap RB channels for the model
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    # Read a frame from the video capture
    success, img = cap.read()

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

    # Wait for a key press and exit if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break
    

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
