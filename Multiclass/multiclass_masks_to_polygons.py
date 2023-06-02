# By: mynguy
# Date: 6/2/2023
# Refer to README to use code correctly

import os
import cv2
import numpy as np

input_dir =    # Input directory: Example- './project/masks'
output_dir =   # Output directory: Example- './project/labels'

# Define the classes and their corresponding color values in the order of the .yaml file
classes = [
    ((52, 209, 183), 'skylight'),
    ((204, 153, 51), 'vent pipe'),
    ((133, 192, 11), 'wind-driven turbine exhaust')
    # Above is an example of some classes used
    # Format: ((R,G,B), 'name of class') Make sure ordering matches your .yaml file.
]

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for image_name in os.listdir(input_dir):
    image_path = os.path.join(input_dir, image_name)
    # Load the binary mask image
    mask = cv2.imread(image_path, cv2.IMREAD_COLOR)

    H, W, _ = mask.shape
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

    # Convert the RGB values of mask to tuples
    mask_rgb_tuples = [tuple(pixel) for pixel in mask_rgb.reshape(-1, 3)]

    # Find unique RGB tuples in the mask image
    unique_rgb_tuples = list(set(mask_rgb_tuples))

    # Filter out tuples not present in the classes list
    valid_rgb_tuples = [rgb_tuple for rgb_tuple in unique_rgb_tuples if rgb_tuple in [c[0] for c in classes]]

    # Initialize the polygons list to store polygons for each class
    polygons = []

    # Find contours for each valid RGB tuple and add them to the polygons list
    for rgb_tuple in valid_rgb_tuples:
        class_name = [c[1] for c in classes if c[0] == rgb_tuple][0]
        mask_rgb_indices = [i for i, x in enumerate(mask_rgb_tuples) if x == rgb_tuple]
        lower_bound = np.array([rgb_tuple[2], rgb_tuple[1], rgb_tuple[0]], dtype=np.uint8)
        upper_bound = np.array([rgb_tuple[2], rgb_tuple[1], rgb_tuple[0]], dtype=np.uint8)
        mask_binary = cv2.inRange(mask, lower_bound, upper_bound)
        mask_contour, _ = cv2.findContours(mask_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in mask_contour:
            if cv2.contourArea(contour) > 200:
                polygon = []
                for point in contour:
                    x, y = point[0]
                    polygon.append(x / W)
                    polygon.append(y / H)
                polygons.append((polygon, class_name))

    if polygons:
        # Save the polygons to the corresponding output file
        output_file = os.path.join(output_dir, '{}.txt'.format(image_name[:-4]))
        with open(output_file, 'w') as f:
            for polygon, class_name in polygons:
                class_number = [c[1] for c in classes].index(class_name)
                f.write('{} '.format(class_number))
                for p in polygon:
                    f.write('{} '.format(p))
                f.write('\n')

    print('Processed:', image_name)

print('Polygon extraction completed.')