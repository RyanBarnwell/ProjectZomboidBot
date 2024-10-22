import mss
import numpy as np
from PIL import Image
import cv2

#screen capture program
def screen_cap(region=None):
    with mss.mss() as sct:
        if region:
            #grab region of screen, unsure how this works with multiple monitors
            screen = sct.grab(region)
        #primary use case currently
        else:
            #if region is undefined grab monitor 1
            screen = sct.grab(sct.monitors[1])
        img = np.array(screen)
        return img