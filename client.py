import socket
import cv2
import numpy as np
import time
from custom_socket import CustomSocket
import json

# image = cv2.imread("dataset/t11.jpg")

cap = cv2.VideoCapture(3)
cap.set(3, 1280)
cap.set(4, 720)

# print(image.shape)
# image = cv2.resize(image, (1280, 720))

host = socket.gethostname()
# host = "192.168.8.2"
port = 10011
c = CustomSocket(host, port)
c.clientConnect()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't read frame.")
        continue

    print("Send")
    msg = c.req(frame)
    print(msg)

    if cv2.waitKey(1) == ord("q"):
        cap.release()

cv2.destroyAllWindows()
