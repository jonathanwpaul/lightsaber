import cv2
import os

# Load the reference image
ref = cv2.imread("src/6.jpg", cv2.IMREAD_GRAYSCALE)

# Get the list of all images in the source folder
src_folder = "src"
images = [f for f in os.listdir(src_folder) if f.endswith(".jpg")]

# Loop through each image in the source folder
for image_name in images:
    # Load the image
    img = cv2.imread(os.path.join(src_folder, image_name), cv2.IMREAD_GRAYSCALE)
    
    # Equalize the histogram of the image to match the reference image
    equalized_img = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)).apply(img)
    
    # Save the equalized image
    cv2.imwrite(os.path.join("equalized", image_name), equalized_img)
