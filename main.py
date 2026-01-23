import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import os
import absl.logging

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
absl.logging.set_verbosity(absl.logging.ERROR)

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

last_volume = 50
is_muted = False
is_paused = False

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            h, w, _ = img.shape
            for id, lm in enumerate(handLms.landmark):
                lmList.append((int(lm.x * w), int(lm.y * h)))

            if lmList:
                x1, y1 = lmList[4]
                x2, y2 = lmList[8]
                length = np.hypot(x2 - x1, y2 - y1)

                volPercent = np.interp(length, [20, 200], [0, 100])
                last_volume = volPercent
                if not is_muted:
                    volume.SetMasterVolumeLevelScalar(volPercent/100, None)

                if length < 30:
                    is_paused = not is_paused
                    cv2.putText(img, "PAUSE/PLAY toggled", (200,50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                    cv2.waitKey(300)

                elif length > 150:
                    is_muted = not is_muted
                    if is_muted:
                        volume.SetMasterVolumeLevelScalar(0, None)
                    else:
                        volume.SetMasterVolumeLevelScalar(last_volume/100, None)
                    cv2.putText(img, f"MUTE toggled: {is_muted}", (200,80),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                    cv2.waitKey(300)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    else:
        if not is_muted:
            volume.SetMasterVolumeLevelScalar(last_volume/100, None)
        cv2.putText(img, "No hand detected, using last volume", (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

    volBar = np.interp(last_volume, [0, 100], [400, 150])
    color = (int(last_volume*2.55), 255 - int(last_volume*2.55), 0)
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), color, cv2.FILLED)
    cv2.putText(img, f'Vol: {int(last_volume)} %', (40, 450),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
