# given a set of pictures (to be used for lithophanes), adjust the brightness of each to be the same average value
# 
import cv2
import os
from cv2 import COLOR_BGR2HSV, COLOR_BGR2GRAY
import numpy as np

def adjust_intensity(image, factor):
    return cv2.convertScaleAbs(image, alpha=factor, beta=0)

src_folder = "src"
desired_brightness = 150

for filename in os.listdir(src_folder):
    
    if filename.endswith(".jpg") or filename.endswith(".png"):
    
        image = cv2.imread(os.path.join(src_folder, filename))
    
        cvt_image = cv2.cvtColor(image, code=COLOR_BGR2HSV)
        averageV  = np.average(cvt_image[2])
        # print("convert_: ", cvt_image[0][0])
        # print("original: ", image[0][0])

        # print("average V: ", averageV )
        
        intensity_factor = desired_brightness/averageV
        adjusted = adjust_intensity(image, intensity_factor)
        gray_adjusted = cv2.cvtColor(adjusted, code=COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join('out', "adjusted_" + filename), gray_adjusted)

print("Intensity adjustment complete.")
