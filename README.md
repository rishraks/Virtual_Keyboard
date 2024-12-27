# Hand Tracking Virtual Keyboard

This project implements a virtual keyboard using hand tracking. By hovering your fingertip over predefined virtual keys, the corresponding letters are typed in Notepad. The project uses computer vision and hand tracking for interaction without physical contact.

## Features

- Tracks the fingertip using a webcam and MediaPipe.
- Detects hovering over virtual keys (`Q` and `W`) and types them in Notepad.
- Visual feedback when hovering over or selecting keys.
- Interactive UI displayed via OpenCV.

## Libraries Used

The following libraries are required:

- **opencv-python**: For capturing video and displaying the interactive UI.
- **mediapipe**: For hand landmark detection and tracking.
- **pyautogui**: For simulating key presses.
- **subprocess**: For launching Notepad.

## How It Works

1. **Initialization**:
   - Launches Notepad on startup using the `subprocess` library.
   - Initializes the webcam for capturing real-time video.
2. **Hand Tracking**:
   - Uses MediaPipe to detect and track the user's hand.
   - Tracks the index fingertip position for interaction.
3. **Virtual Keyboard**:
   - Displays buttons for `Q` and `W` on the screen.
   - Changes button color when the fingertip hovers over a button.
   - Types the corresponding key in Notepad if the hover time exceeds a threshold.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/rishraks/Virtual_Keyboard.git
    ```
2. Install the required libraries:
    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

## Usage

1. Run the script:
    ```bash
    python Virtual_Keyboard.py
    ```
2. Allow access to your webcam.
3. Hover your fingertip over the virtual keys (Q or W or anykey) to type them in Notepad.

## Customization

- Modify the buttons array in the script to add more keys or change button positions.
- Adjust the threshold_time variable to change the hover duration required for a keypress.

## Requirements

- Python 3.7 or higher
- Webcam for hand tracking
- Windows OS (for Notepad integration)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- MediaPipe for their hand tracking API.
- OpenCV for providing real-time video processing tools.
- PyAutoGUI for simulating keyboard inputs.
