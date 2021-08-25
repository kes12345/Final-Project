import cv2
from array import array
import numpy as np
from math import *

cap = cv2.VideoCapture('in.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

pk = 0
while True:
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=8)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue
    #
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)

        center = (x + w // 2, y + h // 2)
        if pk == 0:
            a = np.array([[center[0], center[1]]])
            pk = 1

        else:
            b = np.array([[center[0], center[1]]])
            a = np.concatenate((a,b), axis=0)

        radius = 2
        cv2.circle(frame1, center, radius, (255, 255, 0), 2)

    #cv2.drawContours(frame1, contours, -1, (0,255,0), 3)


        # cv2.imshow('inter', frame1)


    print(a)
    pk = 0

    zx = 0
    for mn in a:
        zx = zx + 1
    i = 0
    zx = zx - 1
    cv = i
    for mn in a:
        for k in range(zx):
            misc = sqrt(abs(((a[cv + 1][0] - a[i][0]) ** 2) + ((a[cv + 1][1] - a[i][1]) ** 2)))

            if(misc < 100):
                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    if cv2.contourArea(contour) < 700:
                        continue

                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)


            cv2.imshow('inter', frame1)

            cv = cv + 1
            print(misc)

        i = i + 1
        cv = i
        zx = zx - 1

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(100) == 27:
        break

cv2.destroyAllWindows()
cap.release()