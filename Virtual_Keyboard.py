import cv2
import mediapipe as mp
import time
import pyautogui
import subprocess


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

subprocess.Popen("notepad.exe")

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.4,
    min_tracking_confidence=0.5,
    static_image_mode=False,
)


cap = cv2.VideoCapture(0)


buttons = [
    {"key": "Q", "start": (100, 180), "end": (200, 250), "color": (51, 51, 53), "coord": (138, 228), "typed": False,"textColor":(255,255,255)},
    {"key": "W", "start": (230, 180), "end": (330, 250), "color": (51, 51, 53), "coord": (268, 228), "typed": False,"textColor":(255,255,255)},
    {"key":"E","start":(360, 180),"end":(460, 250),"color":(51, 51, 53),"coord":(398, 228),"typed":False,"textColor":(255,255,255)},
    {"key": "R", "start": (490, 180), "end": (590, 250), "color": (51, 51, 53), "coord": (528, 228), "typed": False, "textColor": (255, 255, 255)},
    {"key": "T", "start": (620, 180), "end": (720, 250), "color": (51, 51, 53), "coord": (660, 228), "typed": False, "textColor": (255, 255, 255)},
    {"key": "Y", "start": (750, 180), "end": (850, 250), "color": (51, 51, 53), "coord": (788, 228), "typed": False, "textColor": (255, 255, 255)},
    {"key": "U", "start": (880, 180), "end": (980, 250), "color": (51, 51, 53), "coord": (918, 228), "typed": False, "textColor": (255, 255, 255)},
    {"key": "I", "start": (1010, 180), "end": (1110, 250), "color": (51, 51, 53), "coord": (1056, 228), "typed": False, "textColor": (255, 255, 255)},
    {"key": "O", "start": (1140, 180), "end": (1240, 250), "color": (51, 51, 53), "coord": (1178, 228), "typed": False, "textColor": (255, 255, 255)},
    {"key": "P", "start": (1270, 180), "end": (1370, 250), "color": (51, 51, 53), "coord": (1308, 228), "typed": False, "textColor": (255, 255, 255)},
    {"key": "A", "start": (100, 310), "end": (200, 380), "color": (51, 51, 53), "coord": (138, 358), "typed": False, "textColor": (255, 255, 255)},
    {"key": "S", "start": (230, 310), "end": (330, 380), "color": (51, 51, 53), "coord": (268, 358), "typed": False, "textColor": (255, 255, 255)},
    {"key": "D", "start": (360, 310), "end": (460, 380), "color": (51, 51, 53), "coord": (398, 358), "typed": False, "textColor": (255, 255, 255)},
    {"key": "F", "start": (490, 310), "end": (590, 380), "color": (51, 51, 53), "coord": (528, 358), "typed": False, "textColor": (255, 255, 255)},
    {"key": "G", "start": (620, 310), "end": (720, 380), "color": (51, 51, 53), "coord": (660, 358), "typed": False, "textColor": (255, 255, 255)},
    {"key": "H", "start": (750, 310), "end": (850, 380), "color": (51, 51, 53), "coord": (788, 358), "typed": False, "textColor": (255, 255, 255)},
    {"key": "J", "start": (880, 310), "end": (980, 380), "color": (51, 51, 53), "coord": (918, 358), "typed": False, "textColor": (255, 255, 255)},
    {"key": "K", "start": (1010, 310), "end": (1110, 380), "color": (51, 51, 53), "coord": (1056, 358), "typed": False, "textColor": (255, 255, 255)},
    {"key": "L", "start": (1140, 310), "end": (1240, 380), "color": (51, 51, 53), "coord": (1178, 358), "typed": False, "textColor": (255, 255, 255)},
    {"key": "Z", "start": (100, 440), "end": (200, 510), "color": (51, 51, 53), "coord": (138, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key": "X", "start": (230, 440), "end": (330, 510), "color": (51, 51, 53), "coord": (268, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key": "C", "start": (360, 440), "end": (460, 510), "color": (51, 51, 53), "coord": (398, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key": "V", "start": (490, 440), "end": (590, 510), "color": (51, 51, 53), "coord": (528, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key": "B", "start": (620, 440), "end": (720, 510), "color": (51, 51, 53), "coord": (660, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key": "N", "start": (750, 440), "end": (850, 510), "color": (51, 51, 53), "coord": (788, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key": "M", "start": (880, 440), "end": (980, 510), "color": (51, 51, 53), "coord": (918, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key": ",", "start": (1010, 440), "end": (1110, 510), "color": (51, 51, 53), "coord": (1056, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key": ".", "start": (1140, 440), "end": (1240, 510), "color": (51, 51, 53), "coord": (1178, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key": "?", "start": (1270, 440), "end": (1370, 510), "color": (51, 51, 53), "coord": (1308, 488), "typed": False, "textColor": (255, 255, 255)},
    {"key":"backspace","start":(1130, 50),"end":(1360,150),"color":(51, 51, 53),"coord":(1165, 110),"typed":False,"textColor":(255,255,255)},
    {"key":"space","start":(100, 550),"end":(1240, 600),"color":(51,51,53),"coord":(570, 586),"typed":False,"textColor":(255,255,255)}
]
color = (51,51,53)
press_color = (255,255,255)
hover_color = (90, 90, 92)
text_color = (255, 255, 255)
text_press_color = (0,0,0)
threshold_time = 0.2 

hover_start_times = {button["key"]: None for button in buttons}

while True:
    ret, frame = cap.read()
    if not ret:
        break
    else:
        # Prepare the frame
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (1440, 810))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        x, y = 0, 0  
        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                h, w, c = frame.shape
                x = int(handlms.landmark[8].x * w)
                y = int(handlms.landmark[8].y * h)
                cv2.circle(frame, (x, y), 10, (255, 0, 255), cv2.FILLED)
        
        current_time = time.time()  

        for button in buttons:
            start = button["start"]
            end = button["end"]
            is_hovering = start[0] < x < end[0] and start[1] < y < end[1]
            
            if is_hovering:
                if not button["typed"]: 
                    if hover_start_times[button["key"]] is None:
                        hover_start_times[button["key"]] = current_time 
                        button["color"] = hover_color
                    elif current_time - hover_start_times[button["key"]] >= threshold_time:
                        button["color"] = press_color 
                        button["textColor"] = text_press_color
                        if button["key"] == "backspace":
                            pyautogui.press(button["key"])
                        elif button["key"] == "space":
                            pyautogui.typewrite(" ")
                        else:
                            pyautogui.typewrite(button["key"])
                        button["typed"] = True  
                else:
                    button["color"] = press_color  
                    button["textColor"] = text_press_color
            else:

                hover_start_times[button["key"]] = None
                button["color"] = color
                button["textColor"] = text_color
                button["typed"] = False
            
            
            cv2.rectangle(frame, start, end, button["color"], cv2.FILLED)
            cv2.putText(frame, button["key"], button["coord"], cv2.FONT_HERSHEY_SIMPLEX, 1, button["textColor"], 2)
            

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
