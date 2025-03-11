#region imports
#multiple screenshots module
import mss
import numpy as np
#PIL- Image Processing
from PIL import Image
#computer Vision Library
import cv2
#input lib
from pynput.keyboard import Key, Controller, Listener
import random
import time
#endregion

#Loads YOLO Deep Learning Algorithm into OpenCV DNN module
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")

#region Movement
#Init keyboard
keyboard = Controller()

#global movement vars
MOVEMENT_KEYS = ['w', 'a', 's', 'd']

def move():
    img = screen_cap()
    while True:
        key = random.choice(MOVEMENT_KEYS)
        keyboard.press(key)
        time.sleep(random.uniform(0.5, 2.0))
        keyboard.release(key)

        time.sleep(random.uniform(0.2, 1.0))
#endregion


#zombie detection
def detect_zombie(img):
    #use image process to extract edges
    edges = process_image(img)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    zombie_positions = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Define a size threshold to filter out small objects
        if w * h > 1000:
            zombie_positions.append((x + w // 2, y + h // 2))  # Zombie center

    return zombie_positions[0] if zombie_positions else None
    
#screen capture program
def screen_cap(region=None):
    #initializes mss and uses context manager for cleanup
    with mss.mss() as sct:
        #if region is undefined grab monitor 1
        screen = sct.grab(region or sct.monitors[1])
        #Convert img to numpy array
        img = np.array(screen)
        #remove alpha channel
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

#processes image
def process_image(img):
    #convert to greyscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Canny Edge Detection, finds edges
    edges = cv2.Canny(gray, 100, 200)
    return edges


move()