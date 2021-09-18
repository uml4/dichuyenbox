import cv2
from HandTrackingModule import HandDetector

import numpy as np
import Utils


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200




while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:
        # TH 1. thay đổi màu khi click vào box
        # cursor = lmList[8]  # index finger tip landmark
    #     if 100 < cursor[0] < 300 and 100 < cursor[1] < 300:
    #         colorR = 0,255,0
    #     else:
    #         colorR = 255,0,255  

    # cv2.rectangle(img,(100,100), (300,300), colorR,cv2.FILLED)

    # TH 2. di chuyển box theo ngón trỏ
        # cursor = lmList[8]  # index finger tip landmark
    #     if cx-w // 2  < cursor[0] < cx + w // 2 and \
    #         cy -h // 2 < cursor[1] < cy + h // 2:
    #             colorR = 0,255,0
    #             cx, cy = cursor
    #     else:
    #         colorR = 255,0,255  

    # cv2.rectangle(img,(cx-w // 2 ,cy -h // 2), 
    #             (cx + w // 2,cy + h // 2), colorR,cv2.FILLED)

    # TH 3. di chuyển box khi khoảng cách giua ngón trỏ và ngón giữa  <40
        l, _, _ = detector.findDistance(8,12,img)
        print(l)

        if l <40:
            cursor = lmList[8]
            if cx-w // 2  < cursor[0] < cx + w // 2 and \
                cy -h // 2 < cursor[1] < cy + h // 2:
                    colorR = 0,255,0
                    cx, cy = cursor
            else:
                colorR = 255,0,255  

        cv2.rectangle(img,(cx-w // 2 ,cy -h // 2), 
                    (cx + w // 2,cy + h // 2), colorR,cv2.FILLED)



    cv2.imshow("Image", img)
    cv2.waitKey(1)