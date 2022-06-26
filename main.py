import numpy as np
import cv2 as cv

cap = cv.VideoCapture('media/aruco_test_1.mp4')


while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.resize(frame, (1280, 720), interpolation=cv.INTER_AREA)

    if not ret:
        break
    cv.imshow('Aruco Test', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()