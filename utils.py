import mediapipe as mp

class HandGestureProcessor:
    def __init__(self):
        # Finger Tip Landmarks (MediaPipe IDs)
        self.tip_ids = [8, 12, 16, 20] # Index, Middle, Ring, Pinky
        # Finger PIP (Middle Joint) Landmarks
        self.pip_ids = [6, 10, 14, 18]

    def get_finger_status(self, hand_landmarks):
        """
        Returns a list of booleans indicating if a finger is open (True) or closed (False).
        Logic: Tip must be higher (lower Y value) than the PIP joint.
        """
        fingers = []
        
        # Check Thumb (Special case: check X-coordinate distance from palm)
        # Assuming right hand; for general use, we stick to the 4 main fingers for stability
        for i in range(len(self.tip_ids)):
            if hand_landmarks.landmark[self.tip_ids[i]].y < hand_landmarks.landmark[self.pip_ids[i]].y:
                fingers.append(True)
            else:
                fingers.append(False)
        return fingers

    def parse_gesture(self, fingers):
        """
        Translates finger boolean list into a named gesture.
        fingers[0]=Index, [1]=Middle, [2]=Ring, [3]=Pinky
        """
        # 1. Next Slide: Only Index Finger Up
        if fingers[0] and not any(fingers[1:]):
            return "NEXT"
        
        # 2. Previous Slide: Index and Middle Fingers Up
        elif fingers[0] and fingers[1] and not any(fingers[2:]):
            return "PREVIOUS"
        
        # 3. Exit: All Fingers Folded (Fist)
        elif not any(fingers):
            return "EXIT"
        
        return "UNKNOWN"

def draw_info_box(frame, text, color=(0, 255, 0)):
    """
    Helper to draw a styled HUD on the screen.
    """
    import cv2
    cv2.rectangle(frame, (10, 10), (400, 70), (0, 0, 0), -1)
    cv2.putText(frame, f"STATUS: {text}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
