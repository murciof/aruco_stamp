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
    #frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = cv.aruco.detectMarkers(frame, dict, parameters=params)
    if corners:
        for item_corners, item_ids in zip(corners,ids):
            item_corners = np.array(item_corners, np.int32)
            cv.polylines(frame, item_corners, True, (0, 0, 255), 4, cv.LINE_AA)
            print(item_corners, item_ids)
    cv.imshow('Aruco Test', frame)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()