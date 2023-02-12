import cv2
import os

def adjust_intensity(image, factor):
    return cv2.convertScaleAbs(image, alpha=factor, beta=0)

src_folder = "src"
intensity_factor = 0.5 # adjust as needed

for filename in os.listdir(src_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = cv2.imread(os.path.join(src_folder, filename))
        adjusted = adjust_intensity(image, intensity_factor)
        cv2.imwrite(os.path.join(src_folder, "adjusted_" + filename), adjusted)

print("Intensity adjustment complete.")
