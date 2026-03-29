A high-quality **README.md** is a major part of your evaluation. It should be professional, visually organized, and allow anyone (even a non-coder) to run your project.

Copy and paste the following into a file named `README.md` in your GitHub repository.

---

# Air-Gesture Presentation Controller

An AI-powered Computer Vision tool that allows you to control slide presentations (PowerPoint, Google Slides, PDFs) using real-time hand gestures. No clicker, no mouse, no keyboard—just your hands.

##  Overview
The **Air-Gesture Presentation Controller** uses **MediaPipe** for high-fidelity hand landmark detection and **OpenCV** for real-time video processing. By mapping specific finger orientations to system-level keypresses via **PyAutoGUI**, it turns your webcam into a touchless remote control.

###  Key Features
* **Real-time Hand Tracking:** 21-point landmark detection for high precision.
* **Intuitive Gestures:** Simple, easy-to-remember finger triggers.
* **Visual HUD:** On-screen feedback showing current detection and cooldown status.
* **Universal Compatibility:** Works with any presentation software that uses Arrow Keys and Escape.

---

##  How to Control
| Gesture | Action | Command |
| :--- | :--- | :--- |
| **Index Finger Up** | Next Slide | `Right Arrow` |
| **Index + Middle Up** | Previous Slide | `Left Arrow` |
| **Closed Fist** | Exit Presentation | `Escape` |

> **Note:** To prevent accidental double-skipping, the system includes a **1.5-second cooldown** between actions.

---

##  Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Air-Gesture-Controller.git
cd Air-Gesture-Controller
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Run:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

---

##  Project Structure
* `main.py`: The entry point. Handles the webcam feed, UI overlay, and system triggers.
* `utils.py`: Contains the `HandGestureProcessor` class for modular gesture logic.
* `requirements.txt`: List of necessary Python libraries.
* `Report.pdf`: Detailed documentation on the problem, approach, and findings.

---

##  Technical Stack
* **OpenCV:** Image acquisition and UI rendering.
* **MediaPipe:** Hand landmark detection model.
* **PyAutoGUI:** Cross-platform GUI automation for keypresses.
* **Python:** Core logic and state management.

---

##  Troubleshooting
* **Low Light:** Ensure your hand is well-lit for the landmarks to be detected accurately.
* **Permissions:** On macOS/Windows, you may need to grant the terminal/IDE permission to "Control your computer" (Accessibility) for PyAutoGUI to work.
* **Background:** A plain background works best to avoid interference with hand detection.

---

##  Author
Swaroop Bhowmik *Course: Computer Vision Capstone (VITyarthi)*

3.  **Challenges** (like lighting or gesture overlap).

**Would you like me to draft a structured Project Report for you now?**
