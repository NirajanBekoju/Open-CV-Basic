import requests
import cv2
import numpy as np

# Defining Variables
url = "http://10.42.0.96:8080/shot.jpg"
frame_width = 900
frame_height = 560

# Defining window
cv2.namedWindow("Android Cam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Android Cam", frame_width, frame_height)

while True:
    # Retrieving the image from the url
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    cv2.imshow("Android Cam", img)

    # Condition for the breakage
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()