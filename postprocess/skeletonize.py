import os
import cv2
import numpy                as np
from   tqdm                 import tqdm
from   skimage.morphology   import skeletonize
from   skimage              import img_as_ubyte


data_dir   = "path_to_input_dir"
output_dir = "path_to_output_dir"

os.makedirs(output_dir, exist_ok=True)


for name in tqdm(os.listdir(data_dir)):

    img_path = os.path.join(data_dir, name)
    img      = cv2.imread(img_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold to isolate the white lines
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Convert to format required by skeletonize
    binary = thresh > 0
    # Apply skeletonization
    skeleton = skeletonize(binary)
    # Convert back to uint8
    thinned = img_as_ubyte(skeleton)

    thickness = 2
    kernel  = np.ones((thickness, thickness), np.uint8)
    thinned = cv2.dilate(thinned, kernel, iterations=1)
 
    result = cv2.cvtColor(thinned, cv2.COLOR_GRAY2BGRA)
    # Make black pixels transparent
    result[:,:,3] = thinned

    # Save the result
    cv2.imwrite(os.path.join(output_dir, name), result)