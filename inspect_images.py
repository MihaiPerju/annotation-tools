import os
import sys

#Statistics
extensions = []
problematic_files = []
image_dir = sys.argv[1]

print('Image Directory: ' + image_dir)

#Convert to absolute paths
image_dir = os.path.abspath(image_dir)

# Take each image and see if it has annotation file
for filename in os.listdir(image_dir):

    # Find the XML file name that should be searched
    abs_filename = os.path.join(image_dir,filename)
    filename_without_extension = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    if extension not in extensions:
        extensions.append(extension)

    if extension not in ['.jpg', '.jpeg', '.png']:
        problematic_files.append(filename);
 
print("Found Extensions: ")
print(extensions)
if not problematic_files:
    print("No problematic files")
else:
    print("Problematic Files:")
    for filename in problematic_files:
        print(filename)