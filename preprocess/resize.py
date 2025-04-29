import os
import cv2
from   tqdm  import tqdm


######################
#
######################
def resize_image(input_img_path: str, output_img_path: str) -> bool:
    """
    Desc: 
        Resize the original image to 256x256 pixels and save it to a specified path.
    Args:
        input_img_path (str): Path to the input image file.
        output_img_path (str): Path where the resized image will be saved.
    Returns:
        bool: True if resizing and saving are successful, False otherwise.
    """
    try:
        # Load the image (e.g., 120x120 TIFF) with unchanged channel depth
        input_image = cv2.imread(input_img_path, cv2.IMREAD_UNCHANGED)
        
        # Resize the image to 256x256 using cubic interpolation
        output_image = cv2.resize(input_image, (256, 256), interpolation=cv2.INTER_CUBIC)
        
        # Save the resized image
        cv2.imwrite(output_img_path, output_image)

        return True

    except Exception as copy_ex:
        print(f"An error occurred while resizing: {copy_ex}")
        return False


######################
#
######################
if __name__ == "__main__":

    input_dir  = "path_to_test_dir"
    output_dir = "path_to_output_dir"

    os.makedirs(output_dir, exist_ok=True)

    for filename in tqdm(os.listdir(input_dir)):
        original_img_path = os.path.join(input_dir, filename)
        output_img_path   = os.path.join(output_dir, filename)

        resize_image(original_img_path, output_img_path)
