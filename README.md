# Mask to Polygon Conversion Script

This script is designed to help users convert segmentation masks created through annotation tools, such as CVAT, into polygon .txt files in YOLO format. These files can be used to train models in YOLOv8 for image segmentation tasks.

## What is YOLOv8?
YOLOv8 is a state-of-the-art object detection and image segmentation algorithm. It stands for "You Only Look Once" and version 8 refers to the specific iteration of the YOLO algorithm. YOLOv8 is known for its speed and accuracy in detecting and segmenting objects within images.

## Key Features of this Script
Handling Multiple Classes:

This script is capable of handling multiple classes in the segmentation masks.
It associates each class with a specific RGB color value, allowing for accurate identification and conversion of masks into polygon data.
The classes list in the script should be modified to match the classes and their corresponding color values present in your segmentation masks.
RGB Color-Based Classification:

The script converts the RGB color values of each pixel in the mask image to tuples.
It then identifies unique RGB tuples in the mask and filters out tuples not present in the defined classes list.
This enables the script to extract polygons for each class based on their respective RGB color values.
## Steps to Use the Code
1) Make sure you have the following prerequisites installed:  
  **Python 3.x  
  OpenCV (cv2 module)   
  NumPy (numpy module)**

2) Prepare your input and output directories:

3) Set the input_dir variable to the path of your input directory containing the segmentation masks. For example: input_dir = './project/masks'
4) Set the output_dir variable to the path of your output directory where you want to save the polygon .txt files. For example: output_dir = './project/labels'
   Define the classes and their corresponding color values:

4) In the classes list, add tuples representing the RGB color values and the corresponding class names. Make sure the ordering matches your .yaml file or the annotation tool used. 

For example:
```python:
classes = [
    ((52, 209, 183), 'skylight'),
    ((204, 153, 51), 'vent pipe'),
    ((133, 192, 11), 'wind-driven turbine exhaust')
    # Add more classes if needed
]
```

5) Run the script:

Execute the script using a Python interpreter.
The script will process each mask image in the input directory.
For each mask image, it will convert the binary mask to polygons for each class based on the defined color values.
The resulting polygon data will be saved as .txt files in the output directory, following the YOLO format.
Customize for your use case:

Adjust the classes list according to your specific use case and the classes present in your segmentation masks.
Modify the input_dir and output_dir variables to match the directories in your project.
Please refer to the comments within the script for more detailed explanations of each step and additional code documentation.

Note: Make sure to have a good understanding of the YOLOv8 algorithm and how it handles image segmentation before using this script.

By: My Nguyen with support from @computervisioneng and ChatGPT
