import numpy as np
import cv2 as cv
import math

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
            #print(item_corners, item_ids)
            top_left = item_corners[0][0]
            bottom_right = item_corners[0][2]
            print("=========")
            print("Top Left -", top_left)
            #print("Top Right -", item_corners[0][1])
            print("Bottom Right -", bottom_right)
            #print("Bottom Left -", item_corners[0][3])
            coordinates_x = [top_left[0], bottom_right[0]]
            coordinates_x.sort()
            print("Coordinates X -", coordinates_x)
            coordinates_y = [top_left[1], bottom_right[1]]
            coordinates_y.sort()
            print("Coordinates Y -", coordinates_y)
            x_length = coordinates_x[1] - coordinates_x[0]
            #y_length = coordinates_y[1] - coordinates_y[0]
            #square_area = x_length * y_length
            diagonal_length = x_length * math.sqrt(2)
            print("Diagonal -", diagonal_length)
            
    cv.imshow('Aruco Test', frame)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()