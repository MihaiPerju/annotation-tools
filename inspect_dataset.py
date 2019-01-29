import os
import sys

#Statistics
problematic_images =[]
problematic_annotations = [] 

image_dir = sys.argv[1]
annotation_dir = sys.argv[2]

print('Image Directory: ' + image_dir)
print('Annotation Directory: ' + annotation_dir)

#Convert to absolute paths
image_dir = os.path.abspath(image_dir)
annotation_dir = os.path.abspath(annotation_dir)

# Take each image and see if it has annotation file
for filename in os.listdir(image_dir):

    # Find the XML file name that should be searched
    abs_filename = os.path.join(image_dir,filename)
    filename_without_extension = os.path.splitext(filename)[0]
    searched_image_name = os.path.join(annotation_dir,filename_without_extension)
    xml_filename = searched_image_name+".xml"

    # If the XML file doesnt exist - collect name
    if not os.path.isfile(xml_filename):
        problematic_images.append(filename)

# Take each annotation and see if it has annotation file
for filename in os.listdir(annotation_dir):

    # Find the XML file name that should be searched
    abs_filename = os.path.join(annotation_dir,filename)
    filename_without_extension = os.path.splitext(filename)[0]
    searched_annotation_name = os.path.join(image_dir,filename_without_extension)
    image_filename = searched_annotation_name+".jpg"

    # If the image file doesnt exist - collect name
    if not os.path.isfile(image_filename):
        problematic_annotations.append(filename)

print("Problematic Images:")
print(problematic_images)

print("Problematic Annotation:")
print(problematic_annotations)