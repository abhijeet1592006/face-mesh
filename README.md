# Face Mesh Landmarks

This is a base project built by **Abhijeet Singh** that uses MediaPipe's Face Mesh **468 facial landmarks** in real-time using a webcam.
---
## Overview

This program:
- Captures video from the webcam
- Uses MediaPipe's FaceMesh solution
- Identifies 468 facial landmarks per detected face
- Draws green circles on each landmark
- Displays the annotated video stream live

## 📦 Requirements

Make sure you have the following Python libraries installed:

```bash
pip install opencv-python mediapipe
```

## 🚀 How to Run

Clone this repository or copy the code into a .py file.
Run the script:
```bash
python filename.py
```
Press q to quit the video feed.

**⚠️ Make sure your webcam is connected and accessible.**

**Check For Correct Index**

**replace 0 with your camera device index**
```bash
# Start video capture
cap = cv2.VideoCapture(0)
```
## Sample Output
Each face detected will have 468 dots (landmarks) drawn, tracking features like eyes, lips, and facial contours in real time.


## FaceMesh Reference
**MediaPipe FaceMesh provides:**

- 468 facial landmarks

- Face geometry in 3D

- Real-time tracking performance

## Useful for applications in:

- AR filters

- Facial expression detection

- Face-based gesture controls

- 3D face modeling

## 📄 License
This project is open source and available under the MIT License.

## Built by Abhijeet Singh
**Powered by OpenCV & MediaPipe**
