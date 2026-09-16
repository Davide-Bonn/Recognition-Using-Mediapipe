<div align="center">

# Recognition Using MediaPipe

**Real-time computer vision demos — hand tracking, face detection, pose estimation, and eye mesh**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

*Four standalone demos running live from your webcam. Press `q` to quit any script.*

---

</div>

## Overview

This repository contains four self-contained computer vision demos built with MediaPipe and OpenCV. Each script captures webcam input and applies a different MediaPipe solution in real time — from hand landmark detection to full-body pose estimation. They serve as clear, minimal examples of how to integrate MediaPipe into Python projects.

---

## Demos

| Script | What It Does | Landmarks |
|:---|:---|:---|
| `Handtracking.py` | Detects hands, draws 21 landmarks per hand with connections, highlights thumb tip, displays FPS | 21 per hand |
| `Facedetection.py` | Detects faces, draws bounding boxes with confidence percentages, displays FPS | 6 keypoints |
| `Posetracking.py` | Detects 33 body pose landmarks, draws full skeleton, displays FPS | 33 |
| `EyeRecognition.py` | Draws all 478 face mesh landmarks, highlights key eye landmarks (145, 159) | 478 |

---

## How It Works

```
Webcam Frame --> BGR to RGB --> MediaPipe Process --> Draw Landmarks --> Display
```

Each script follows the same pipeline: capture a frame from the webcam, convert it from BGR to RGB for MediaPipe processing, run the relevant MediaPipe solution, draw the detected landmarks back onto the frame, and display the result in a window.

---

## MediaPipe Solutions Used

| Solution | Script | Description |
|:---|:---|:---|
| Hands | `Handtracking.py` | Detects up to 2 hands with 21 landmarks each |
| Face Detection | `Facedetection.py` | Lightweight face detector with 6 keypoints |
| Pose | `Posetracking.py` | Full-body pose estimation with 33 landmarks |
| Face Mesh | `EyeRecognition.py` | Dense 478-point face mesh for detailed facial feature tracking |

---

## Quick Start

```bash
git clone https://github.com/Davide-Bonn/Recognition-Using-Mediapipe.git
cd Recognition-Using-Mediapipe
pip install -r requirements.txt
```

Run any demo:

```bash
python Handtracking.py
python Facedetection.py
python Posetracking.py
python EyeRecognition.py
```

Press `q` to quit.

---

## Dependencies

- `mediapipe`
- `opencv-contrib-python`
- `pyautogui`

---

## Related Projects

- [MouseEye](https://github.com/Davide-Bonn/MouseEye) — Eye-controlled mouse built on top of these demos

---

## License

MIT
