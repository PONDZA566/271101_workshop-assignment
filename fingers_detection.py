import cv2
import mediapipe as mp

fin = "None"
fingers = ["None","Thumb","Index","Middle","Ring","Pinky"]
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                elif id == 3:
                    id3 = int(id)
                    cx3 = cx
                elif id == 8:
                    id8 = int(id)
                    cx8 = cx
                elif id == 7:
                    id7 = int(id)
                    cx7 = cx
                elif id == 12:
                    id12 = int(id)
                    cx12 = cx
                elif id == 11:
                    id11 = int(id)
                    cx11 = cx
                elif id == 16:
                    id16 = int(id)
                    cx16 = cx
                elif id == 15:
                    id15 = int(id)
                    cx15 = cx
                elif id == 20:
                    id20 = int(id)
                    cx20 = cx
                elif id == 19:
                    id19 = int(id)
                    cx19 = cx
        if cx4 > cx3 and cx8 > cx7 and cx12 > cx11 and cx16 > cx15 and cx20 > cx19:
            fin = fingers[1] + fingers[2] + fingers[3] + fingers[4] + fingers[5]
        elif cx8 > cx7 and cx12 > cx11 and cx16 > cx15 and cx20 > cx19:
            fin = fingers[2] + fingers[3] + fingers[4] + fingers[5]
        elif cx4 > cx3 and cx12 > cx11 and cx16 > cx15 and cx20 > cx19:
            fin = fingers[1] + fingers[3] + fingers[4] + fingers[5]
        elif cx8 > cx7 and cx4 > cx3 and cx16 > cx15 and cx20 > cx19:
            fin = fingers[1] + fingers[2] + fingers[4] + fingers[5]
        elif cx8 > cx7 and cx12 > cx11 and cx4 > cx3 and cx20 > cx19:
            fin = fingers[1] + fingers[2] + fingers[3] + fingers[5]
        elif cx8 > cx7 and cx12 > cx11 and cx16 > cx15 and cx4 > cx3:
            fin = fingers[1] + fingers[2] + fingers[3] + fingers[4]
        elif cx4 > cx3 and cx8 > cx7 and cx12 > cx11:
            fin = fingers[1] + fingers[2] + fingers[3]
        elif cx4 > cx3 and cx8 > cx7 and cx16 > cx15:
            fin = fingers[1] + fingers[2] + fingers[4]
        elif cx4 > cx3 and cx8 > cx7 and cx20 > cx19:
            fin = fingers[1] + fingers[2] + fingers[5]
        elif cx16 > cx15 and cx8 > cx7 and cx12 > cx11:
            fin = fingers[2] + fingers[3] + fingers[4]
        elif cx20 > cx19 and cx8 > cx7 and cx12 > cx11:
            fin = fingers[2] + fingers[3] + fingers[5]
        elif cx16 > cx15 and cx20 > cx19 and cx12 > cx11:
            fin = fingers[3] + fingers[4] + fingers[5]
        elif cx4 > cx3 and cx8 > cx7:
            fin = fingers[1] + fingers[2]
        elif cx4 > cx3 and cx12 > cx11:
            fin = fingers[1] + fingers[3]
        elif cx4 > cx3 and cx16 > cx15:
            fin = fingers[1] + fingers[4]
        elif cx4 > cx3 and cx20 > cx19:
            fin = fingers[1] + fingers[5]
        elif cx8 > cx7 and cx12 > cx11:
            fin = fingers[2] + fingers[3]
        elif cx8 > cx7 and cx16 > cx15:
            fin = fingers[2] + fingers[4]
        elif cx8 > cx7 and cx20 > cx19:
            fin = fingers[2] + fingers[5]
        elif cx12 > cx11 and cx16 > cx15:
            fin = fingers[3] + fingers[4]
        elif cx12 > cx11 and cx20 > cx19:
            fin = fingers[3] + fingers[5]
        elif cx16 > cx15 and cx20 > cx19:
            fin = fingers[4] + fingers[5]
        elif cx4 > cx3:
            fin = fingers[1]
        elif cx8 > cx7:
            fin = fingers[2]
        elif cx12 > cx11:
            fin = fingers[3]
        elif cx16 > cx15:
            fin = fingers[4]
        elif cx20 > cx19:
            fin = fingers[5]
        else:
            fin = fingers[0]
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cv2.putText(img, fin, (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)