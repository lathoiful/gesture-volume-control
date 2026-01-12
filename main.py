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
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
                cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

                length = np.hypot(x2 - x1, y2 - y1)

                volPercent = np.interp(length, [20, 200], [0, 100])
                volume.SetMasterVolumeLevelScalar(volPercent / 100, None)

                volBar = np.interp(volPercent, [0, 100], [400, 150])
                cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
                cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)

                cv2.putText(img, f'Vol: {int(volPercent)} %', (40, 450),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
