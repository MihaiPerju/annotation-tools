import os
import sys

#Statistics
types = []

image_dir = sys.argv[1]

print('Image Directory: ' + image_dir)

#Convert to absolute paths
image_dir = os.path.abspath(image_dir)

# Take each image and see if it can be processed by OpenCV
for filename in os.listdir(image_dir):
    img = cv2.imread(image_dir)
    if type(img) not in types:
        types.append(type(img))
    
print("Types of images: ")
print(types)