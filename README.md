<div align="center">

# Recognition Using MediaPipe

**Real-time computer vision demos powered by MediaPipe and OpenCV.**

Face detection, hand tracking, pose estimation, eye/face mesh recognition, and an eye-controlled mouse — all running live from your webcam.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)

---

</div>

## Overview

Five standalone Python scripts that demonstrate core MediaPipe solutions using your webcam. Each script opens a live video feed, processes frames in real time, and draws the detected landmarks or bounding boxes directly on screen.

Press **`q`** to quit any script.

---

## Scripts

| Script | What it does |
|--------|-------------|
| **`Handtracking.py`** | Detects hands and draws 21 landmarks per hand with connections. Highlights the thumb tip (landmark 4) with a larger circle. Displays FPS. |
| **`Facedetection.py`** | Detects faces and draws bounding boxes with confidence percentages. Displays FPS. |
| **`Posetracking.py`** | Detects 33 body pose landmarks and draws the full skeleton with connections. Displays FPS. |
| **`EyeRecognition.py`** | Draws all 478 face mesh landmarks and highlights key eye landmarks (145, 159) for left eye tracking. |
| **[`MouseEye/`](MouseEye/)** | Eye-controlled mouse — move the cursor with your iris, left-eye blink to left-click, right-eye blink to right-click. [See full docs →](MouseEye/README.md) |

---

## How It Works

Each script follows the same pipeline:

```
Webcam Frame → BGR to RGB → MediaPipe Processing → Draw Landmarks → Display
```

1. **Capture** — OpenCV reads frames from the default webcam (`VideoCapture(0)`)
2. **Convert** — Frames are converted from BGR to RGB (MediaPipe expects RGB input)
3. **Process** — The relevant MediaPipe solution analyzes the frame and returns landmarks
4. **Draw** — Landmarks, bounding boxes, or connections are drawn onto the original frame
5. **Display** — The annotated frame is shown in an OpenCV window

---

## MediaPipe Solutions Used

| Solution | Script | Landmarks | Description |
|----------|--------|-----------|-------------|
| **Hands** | `Handtracking.py` | 21 per hand | Detects hand skeleton — fingertips, knuckles, wrist |
| **Face Detection** | `Facedetection.py` | 6 keypoints | Lightweight face bounding box with confidence score |
| **Face Mesh** | `EyeRecognition.py` | 478 | Dense face mesh with refined iris landmarks |
| **Face Mesh + Iris** | `MouseEye/mouse_eye.py` | 478 + iris | Iris tracking for cursor control, EAR for blink-to-click |
| **Pose** | `Posetracking.py` | 33 | Full body skeleton — shoulders, elbows, hips, knees, ankles |

---

## Quick Start

### Prerequisites

- [Python](https://www.python.org/) 3.8+
- A webcam

### 1. Clone and install

```bash
git clone https://github.com/Davide-Bonn/Recognition-Using-Mediapipe.git
cd Recognition-Using-Mediapipe
pip install mediapipe opencv-contrib-python pyautogui numpy
```

### 2. Run any script

```bash
python Handtracking.py
python Facedetection.py
python Posetracking.py
python EyeRecognition.py
python MouseEye/mouse_eye.py
```

Press **`q`** to close the window.

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `mediapipe` | ML models for hand, face, pose, and mesh detection |
| `opencv-contrib-python` | Webcam capture, image processing, and display |
| `pyautogui` | Screen resolution detection and mouse control (`EyeRecognition.py`, `MouseEye/`) |
| `numpy` | Distance calculations for blink detection (`MouseEye/`) |

---

## Project Structure

```
Recognition-Using-Mediapipe/
  Handtracking.py      # Hand landmark detection (21 points per hand)
  Facedetection.py     # Face bounding box detection with confidence
  Posetracking.py      # Full body pose estimation (33 landmarks)
  EyeRecognition.py    # Dense face mesh (478 points) with eye tracking
  MouseEye/
    mouse_eye.py       # Eye-controlled mouse with blink-to-click
    logo.svg           # Project logo
    icon.svg           # App icon
    README.md          # MouseEye documentation
  README.md
```

---

## License

Personal project for learning computer vision with MediaPipe.
