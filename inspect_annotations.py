import os
import sys

#Statistics
extensions = []
problematic_files = []
annotation_dir = sys.argv[1]

print('Annotation Directory: ' + annotation_dir)

#Convert to absolute paths
annotation_dir = os.path.abspath(annotation_dir)

# Take each annotation and see if it has annotation file
for filename in os.listdir(annotation_dir):

    # Find the XML file name that should be searched
    abs_filename = os.path.join(annotation_dir,filename)
    filename_without_extension = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    if extension not in extensions:
        extensions.append(extension)

    if extension not in ['.xml']:
        problematic_files.append(filename);
 
print("Found Extensions: ")
print(extensions)
if not problematic_files:
    print("No problematic files")
else:
    print("Problematic Files:")
    for filename in problematic_files:
        print(filename)