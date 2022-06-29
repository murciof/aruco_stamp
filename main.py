from cmath import tan
import numpy as np
import cv2 as cv
import math

cap = cv.VideoCapture('media/aruco_test_1.mp4')

dict = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_50)

params = cv.aruco.DetectorParameters_create()

diagonal_threshold = 100

text_margin = 60

stamped = False

paint_frame = np.zeros([720, 1280, 3], dtype=np.uint8)
paint_frame.fill(255)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.resize(frame, (1280, 720), interpolation=cv.INTER_AREA)
    if not ret:
        break
    #frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = cv.aruco.detectMarkers(frame, dict, parameters=params)
    if corners:
        for item_corners, item_ids in zip(corners,ids):
            stamp = False
            item_corners = np.array(item_corners, np.int32)
            #print(item_corners, item_ids)
            top_left = item_corners[0][0]
            top_right = item_corners[0][1]
            bottom_right = item_corners[0][2]
            bottom_left = item_corners[0][3]
            #print("=========")
            #print("Top Left -", top_left)
            #print("Top Right -", item_corners[0][1])
            #print("Bottom Right -", bottom_right)
            #print("Bottom Left -", item_corners[0][3])
            coordinates_x = [top_left[0], bottom_right[0]]
            coordinates_x_sorted = coordinates_x
            coordinates_x_sorted.sort()
            #print("Coordinates X -", coordinates_x)
            coordinates_y = [top_left[1], bottom_right[1]]
            coordinates_y_sorted = coordinates_y
            coordinates_y_sorted.sort()
            #print("Coordinates Y -", coordinates_y)
            x_delta = coordinates_x_sorted[1] - coordinates_x_sorted[0]
            y_delta = coordinates_y_sorted[1] - coordinates_y_sorted[0]
            #square_area = x_length * y_length
            diagonal_length = x_delta * math.sqrt(2)
            #print("Diagonal -", diagonal_length)

            tangent = - (bottom_right[1] - bottom_left[1]) / (bottom_right[0] - bottom_left[0])

            rotation = math.degrees(math.atan(tangent))

            cv.putText(frame, str(math.trunc(rotation)), (top_left[0], top_left[1]), cv.FONT_HERSHEY_SIMPLEX, 1, (220, 100, 100), 2, cv.LINE_AA)

            if (diagonal_length <= diagonal_threshold) and not stamped:
                stamp_location_coordinates = [coordinates_x_sorted[0] + (x_delta / 2), coordinates_y_sorted[0] + (y_delta / 2)]
                print("=========")
                print("Stamp coordinates:", stamp_location_coordinates)
                print("Rotation:", rotation)
                stamped = True
                cv.line(paint_frame, (top_left[0], top_left[1]), (top_right[0], top_right[1]), (0,0,0), 4)
                cv.polylines(frame, item_corners, True, (0, 255, 0), 8, cv.LINE_AA)
            elif (diagonal_length <= diagonal_threshold) and stamped:
                cv.polylines(frame, item_corners, True, (80, 255, 255), 4, cv.LINE_AA)
            elif (diagonal_length > diagonal_threshold) and stamped:
                stamped = False
            else:
                cv.polylines(frame, item_corners, True, (0, 0, 255), 4, cv.LINE_AA)
    if cv.waitKey(1) == ord('q'):
        break

    cv.imshow('Aruco Test', frame)
    cv.imshow('Painting', paint_frame)


cap.release()
cv.destroyAllWindows()