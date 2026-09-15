import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
CAM_INDEX = 0
SMOOTHING = 4            # higher = smoother but slower cursor
BLINK_THRESHOLD = 0.004  # EAR below this = eye closed
CLICK_COOLDOWN = 15      # frames to wait between clicks

# ---------------------------------------------------------------------------
# Landmark indices (MediaPipe Face Mesh 478-point model)
# ---------------------------------------------------------------------------
# Right eye vertical: top 159, bottom 145
# Right eye horizontal: inner 133, outer 33
RIGHT_EYE = [33, 159, 145, 133]

# Left eye vertical: top 386, bottom 374
# Left eye horizontal: inner 362, outer 263
LEFT_EYE = [263, 386, 374, 362]

# Right iris center
RIGHT_IRIS = [468, 469, 470, 471, 472]
# Left iris center
LEFT_IRIS = [473, 474, 475, 476, 477]


def eye_aspect_ratio(landmarks, eye_indices, fw, fh):
    """Calculate eye aspect ratio (EAR) to detect blinks."""
    pts = []
    for idx in eye_indices:
        lm = landmarks[idx]
        pts.append((lm.x * fw, lm.y * fh))

    # horizontal distance
    horizontal = np.linalg.norm(np.array(pts[0]) - np.array(pts[3]))
    # vertical distance
    vertical = np.linalg.norm(np.array(pts[1]) - np.array(pts[2]))

    if horizontal == 0:
        return 0.0
    return vertical / horizontal


def iris_center(landmarks, iris_indices, fw, fh):
    """Get the average position of iris landmarks."""
    x = sum(landmarks[i].x for i in iris_indices) / len(iris_indices)
    y = sum(landmarks[i].y for i in iris_indices) / len(iris_indices)
    return x * fw, y * fh


# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
cam = cv2.VideoCapture(CAM_INDEX)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

face_mesh = mp.solutions.face_mesh.FaceMesh(
    refine_landmarks=True,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

screen_w, screen_h = pyautogui.size()
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

prev_x, prev_y = screen_w // 2, screen_h // 2
right_cooldown = 0
left_cooldown = 0

print("MouseEye started — move your eyes to control the cursor")
print("Close LEFT eye  -> Left click")
print("Close RIGHT eye -> Right click")
print("Press 'q' to quit")

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
while True:
    success, frame = cam.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    fh, fw, _ = frame.shape
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        # --- Cursor movement via right iris ---
        ix, iy = iris_center(landmarks, RIGHT_IRIS, fw, fh)

        # Map iris position to screen coordinates
        # Iris moves in a small range, so we remap with margins
        margin_x = fw * 0.15
        margin_y = fh * 0.20
        target_x = np.interp(ix, (margin_x, fw - margin_x), (0, screen_w))
        target_y = np.interp(iy, (margin_y, fh - margin_y), (0, screen_h))

        # Smooth the movement
        curr_x = prev_x + (target_x - prev_x) / SMOOTHING
        curr_y = prev_y + (target_y - prev_y) / SMOOTHING
        prev_x, prev_y = curr_x, curr_y

        pyautogui.moveTo(int(curr_x), int(curr_y))

        # --- Blink detection ---
        right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE, fw, fh)
        left_ear = eye_aspect_ratio(landmarks, LEFT_EYE, fw, fh)

        # Decrement cooldowns
        if right_cooldown > 0:
            right_cooldown -= 1
        if left_cooldown > 0:
            left_cooldown -= 1

        # Left eye closed -> left click
        if left_ear < BLINK_THRESHOLD and right_ear >= BLINK_THRESHOLD:
            if left_cooldown == 0:
                pyautogui.click()
                left_cooldown = CLICK_COOLDOWN
                cv2.putText(frame, "LEFT CLICK", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Right eye closed -> right click
        if right_ear < BLINK_THRESHOLD and left_ear >= BLINK_THRESHOLD:
            if right_cooldown == 0:
                pyautogui.click(button='right')
                right_cooldown = CLICK_COOLDOWN
                cv2.putText(frame, "RIGHT CLICK", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # --- Draw on preview ---
        # Draw iris circles
        for idx in RIGHT_IRIS:
            x = int(landmarks[idx].x * fw)
            y = int(landmarks[idx].y * fh)
            cv2.circle(frame, (x, y), 2, (0, 255, 255), -1)
        for idx in LEFT_IRIS:
            x = int(landmarks[idx].x * fw)
            y = int(landmarks[idx].y * fh)
            cv2.circle(frame, (x, y), 2, (0, 255, 255), -1)

        # Draw eye contours
        for idx in RIGHT_EYE:
            x = int(landmarks[idx].x * fw)
            y = int(landmarks[idx].y * fh)
            cv2.circle(frame, (x, y), 2, (255, 0, 255), -1)
        for idx in LEFT_EYE:
            x = int(landmarks[idx].x * fw)
            y = int(landmarks[idx].y * fh)
            cv2.circle(frame, (x, y), 2, (255, 0, 255), -1)

        # EAR display
        cv2.putText(frame, f"L EAR: {left_ear:.4f}", (10, fh - 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f"R EAR: {right_ear:.4f}", (10, fh - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("MouseEye", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
