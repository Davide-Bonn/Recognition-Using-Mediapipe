<div align="center">

<img src="logo.svg" alt="MouseEye Logo" width="280" />

<br/><br/>

# MouseEye

**Control your mouse cursor with your eyes — hands-free.**

Move the cursor by looking around. Blink your left eye to left-click, blink your right eye to right-click.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-FFD43B?style=for-the-badge&logo=python&logoColor=black)](https://pyautogui.readthedocs.io/)

---

</div>

## How It Works

MouseEye uses MediaPipe's **Face Mesh** with the 478-point model (including refined iris landmarks) to track your eye movements in real time.

```
Webcam → Face Mesh (478 landmarks) → Iris Position → Cursor Movement
                                    → Eye Aspect Ratio → Blink → Click
```

| Step | Detail |
|------|--------|
| **Iris Tracking** | The right iris center (landmarks 468–472) is mapped to screen coordinates to move the cursor |
| **Blink Detection** | Eye Aspect Ratio (EAR) measures the vertical-to-horizontal ratio of each eye. When EAR drops below a threshold, the eye is considered closed |
| **Left Click** | Close your **left eye** only (keep right eye open) |
| **Right Click** | Close your **right eye** only (keep left eye open) |
| **Smoothing** | Cursor movement is smoothed with interpolation to prevent jitter |
| **Cooldown** | A 15-frame cooldown prevents repeated clicks from a single blink |

---

## Quick Start

### Prerequisites

- [Python](https://www.python.org/) 3.8+
- A webcam

### 1. Install dependencies

```bash
pip install mediapipe opencv-contrib-python pyautogui numpy
```

### 2. Run

```bash
python mouse_eye.py
```

Press **`q`** to quit.

---

## Configuration

Tune these constants at the top of `mouse_eye.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `SMOOTHING` | `4` | Higher = smoother but slower cursor. Lower = more responsive but jittery |
| `BLINK_THRESHOLD` | `0.004` | EAR value below which an eye is considered closed. Lower = harder to trigger |
| `CLICK_COOLDOWN` | `15` | Frames to wait between clicks. Prevents double-clicks from slow blinks |
| `CAM_INDEX` | `0` | Webcam device index. Change if you have multiple cameras |

---

## Preview Window

The preview window shows:

- **Cyan dots** — Iris landmarks (tracking cursor position)
- **Magenta dots** — Eye corner landmarks (measuring blink ratio)
- **L EAR / R EAR** — Live Eye Aspect Ratio values for each eye
- **LEFT CLICK / RIGHT CLICK** — Flash indicator when a click is triggered

---

## Key Landmarks

```
Right Eye                          Left Eye
  159 (top)                          386 (top)
   |                                  |
33 ---- 133                      263 ---- 362
   |                                  |
  145 (bottom)                       374 (bottom)

Right Iris: 468-472              Left Iris: 473-477
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `mediapipe` | Face Mesh model with 478-point detection and iris refinement |
| `opencv-contrib-python` | Webcam capture, frame processing, preview window |
| `pyautogui` | Mouse cursor movement and click simulation |
| `numpy` | Distance calculations for Eye Aspect Ratio |

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Cursor drifts or jumps | Increase `SMOOTHING` to `6` or `8` |
| Clicks trigger too easily | Lower `BLINK_THRESHOLD` to `0.003` |
| Clicks don't register | Raise `BLINK_THRESHOLD` to `0.005` |
| Double clicks on single blink | Increase `CLICK_COOLDOWN` to `25` |
| Wrong webcam selected | Change `CAM_INDEX` to `1` or `2` |

---

## License

Personal project for learning computer vision with MediaPipe.
