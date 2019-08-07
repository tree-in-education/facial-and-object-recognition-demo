# Object-Recognition-Facial-Recognition
Tech demo for Technology + Ethics

## Object-Recogntion
Object-Recognition will be ran on the Raspberry Pi. Object-Recognition will use Object_detection_picamera.py. Demo requires Tensorflow, OpenCV, and Protobuf.

### Usage
Boot up Raspberry Pi. Make sure camera module is plugged in and propped up on camera stand. To run the object recognition script, navigate to the correct directory:
```
cd /home/pi/tensorflow1/models/research/object_detection
```
Now simply run the script with python3:
```
python3 Object_detection_picamera.py
```
The script will take up to 30 seconds to run. Eventually, a window labeled "Object detector" should pop up. This window shows the view of the camera. It will draw a rectangle around any objects it recognizes, with the name of the object and the % confidence that it is that object. 

### Model Info
The model I am running is called ssdlite_mobilenet_v2_coco. It is a pre-trained model that is optimized for low-power machines. That means it sacrifices a bit of accuracy and frame rate so it can run on the Raspberry Pi, but it works fine for a demo. The model is trained to recognize 90 objects, which are listed here: https://github.com/amikelive/coco-labels/blob/master/coco-labels-paper.txt

### Adjustment
The main adjustment I have made to the model is a single change in labeling. I changed the label of "cell phone" to "gun", which means every time the model recognizes a cell phone, it will label it as "gun". This is to get conversation started by framing an example of a deadly mistake that real humans have made.

## Facial-Recongition
Facial-Recognition will be ran on Macbook Pro. Facial-Recognition uses FaceDetection.py and TakePic.py. Demo requires Tensorflow, OpenCV, and Dlib.

### Usage
This demo uses two scripts, FaceDetection.py and TakePic.py. Both are located in the FacialRecogntion directory. Navigate to the FacialDetection directory to begin:
```
cd FacialDetection
```
Run the FaceDetection.py script.

#### FaceDetection.py
The script will take up to 30 seconds to get started. A camera window will pop up. The camera will draw a green box around any person it recognizes. The camera should recognize a person if their photo is in the facialImages folder. It will label them as whatever the image is named in the folder. Press "q" to quit.

The facialImages folder is located in the FacialRecognition folder.  To enter a new person into the facialImages folder using the webcam, run TakePic.py.

#### TakePic.py
This will bring up another camera window. To take a picture, press the spacebar. The camera window will freeze, and the terminal will ask you to enter your name. Note that the Terminal may be hidden behind the camera window. Once a name is entered, the image will be saved to the facialImages folder, and it will be named whatever you entered. When the camera recognizes you with FacialRecognition.py, this is the name that will pop up. You can take additional pictures while the window is still open. Press "q" to quit.

### facialImages Info
The facialImages folder will be filled with photos of celebrities and random people found from a database online. It is possible that someone could be misidentified. If a person does not have a photo in the facialImages folder, it is likely they will be misidentified, especially if the model strictness has been lowered.

### Adjusting Strictness
On line 10 of FaceDetection.py:
```python
MAX_DISTANCE = 0.6  # increase to make recognition less strict, decrease to make more strict
```
As the comment says. Increase to make it more likely to recognize you as someone, but possibly someone you're not. Decrease to reduce the chance of misidentification. As a guideline, it seems .9 is as loose as you'd need it to be and .2-.3 is as strict as it can be while remaining useful.


