import numpy as np
import cv2 as cv

cap = cv.VideoCapture('media/aruco_test_1.mp4')

dict = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_50)

params = cv.aruco.DetectorParameters_create()


while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.resize(frame, (1280, 720), interpolation=cv.INTER_AREA)
    if not ret:
        break
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = cv.aruco.detectMarkers(frame_gray, dict, parameters=params)
    print(ids)
    cv.imshow('Aruco Test', frame_gray)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()