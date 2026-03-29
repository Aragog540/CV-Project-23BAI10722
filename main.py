import cv2
import mediapipe as mp
import pyautogui
import time

# --- Initialization ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# Screen settings for PyAutoGUI
pyautogui.FAILSAFE = True

# Variables for gesture control
cooldown_time = 1.5  # Seconds between triggers
last_trigger_time = 0

def get_gesture(hand_landmarks):
    """
    Logic: Compare the Y-coordinate of the tip to the middle joint (PIP).
    In OpenCV/MediaPipe, a LOWER Y-value means the point is HIGHER on the screen.
    """
    # Landmark IDs: Index=8, Middle=12, Ring=16, Pinky=20
    # Joint IDs: Index_PIP=6, Middle_PIP=10, Ring_PIP=14, Pinky_PIP=18
    
    fingers = []
    # Index finger
    fingers.append(hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y)
    # Middle finger
    fingers.append(hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y)
    # Ring finger
    fingers.append(hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y)
    # Pinky finger
    fingers.append(hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y)

    # Logic Mapping
    if fingers[0] and not any(fingers[1:]):
        return "NEXT"
    elif fingers[0] and fingers[1] and not any(fingers[2:]):
        return "PREVIOUS"
    elif not any(fingers):
        return "EXIT"
    return None

# --- Main Loop ---
cap = cv2.VideoCapture(0)

print("Presentation Controller Active...")
print("1 Finger -> Next | 2 Fingers -> Previous | Fist -> Exit")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    current_time = time.time()
    status_text = "Waiting..."

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
            
            gesture = get_gesture(hand_lms)
            
            # Trigger action if cooldown has passed
            if gesture and (current_time - last_trigger_time > cooldown_time):
                if gesture == "NEXT":
                    pyautogui.press('right')
                    status_text = "ACTION: NEXT SLIDE"
                    last_trigger_time = current_time
                elif gesture == "PREVIOUS":
                    pyautogui.press('left')
                    status_text = "ACTION: PREVIOUS SLIDE"
                    last_trigger_time = current_time
                elif gesture == "EXIT":
                    pyautogui.press('esc')
                    status_text = "ACTION: EXIT PRESENTATION"
                    last_trigger_time = current_time
            elif gesture:
                status_text = f"Detected: {gesture} (Cooldown)"

    # Overlay UI
    cv2.rectangle(frame, (10, 10), (350, 60), (0, 0, 0), -1)
    cv2.putText(frame, status_text, (20, 45), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Air-Gesture Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
