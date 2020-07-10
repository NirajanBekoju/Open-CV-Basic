import requests
import cv2
import numpy as np

# Defining Variables
url = "http://192.168.43.1:8080/shot.jpg"
frame_width = 900
frame_height = 560

# Defining window
cv2.namedWindow("Android Cam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Android Cam", frame_width, frame_height)

# Retrieving the image from the url
img_resp = requests.get(url)
img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
img = cv2.imdecode(img_arr, -1)

# Setting up and initializing the tracker
tracker = cv2.TrackerMOSSE_create()
bbox = cv2.selectROI("Android Cam",img, False)
tracker.init(img, bbox)

def drawBox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    cv2.putText(img, "Target Detected", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

while True:
    # Setting the timer
    timer = cv2.getTickCount()

    # Retrieving the image from the url
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    # Updating the tracker
    success, bbox = tracker.update(img)

    # if the object is tracked
    if success:
        drawBox(img,bbox)
        print(bbox)
    else:
        cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
    cv2.rectangle(img,(15,15),(200,90),(255,0,255),2)
    cv2.putText(img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2)
    cv2.putText(img, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
 
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    if fps>60: myColor = (20,230,20)
    elif fps>20: myColor = (230,20,20)
    else: myColor = (20,20,230)
    cv2.putText(img,str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2)

    # Showing the Tracking Video
    cv2.imshow('Android Cam', img)

    # Condition for the breakage
    if cv2.waitKey(1) == 27:
        break
