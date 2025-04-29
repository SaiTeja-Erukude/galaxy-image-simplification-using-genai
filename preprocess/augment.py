import os
import cv2
import numpy            as np
from scipy.ndimage      import rotate
from tqdm               import tqdm


######################
#
######################
def augment_img(img_path: str, result_folder_path: str) -> None:
    """
    Desc:
        Applies a series of image augmentations (flip, rotate, blur, brightness, zoom) and
        saves the results in the specified output folder.
    Args:
        img_path (str): Path to the input image.
        result_folder_path (str): Directory to save augmented images.
    Returns:
        None
    """
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        return

    os.makedirs(result_folder_path, exist_ok=True)

    image = cv2.imread(img_path)
    if image is None:
        print(f"Failed to read image: {img_path}")
        return

    filename = os.path.splitext(os.path.basename(img_path))[0]

    # Save original
    cv2.imwrite(os.path.join(result_folder_path, f"{filename}.jpg"), image)

    # Horizontal flip
    flipped_horizontal = cv2.flip(image, 1)
    cv2.imwrite(os.path.join(result_folder_path, f"{filename}_horizontal.jpg"), flipped_horizontal)

    # Vertical flip
    flipped_vertical = cv2.flip(image, 0)
    cv2.imwrite(os.path.join(result_folder_path, f"{filename}_vertical.jpg"), flipped_vertical)

    # 90-degree rotation
    rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(result_folder_path, f"{filename}_rotated90.jpg"), rotated_90)

    # Brightness adjustment (increase)
    brightness_inc = cv2.convertScaleAbs(image, alpha=1.2, beta=10)
    cv2.imwrite(os.path.join(result_folder_path, f"{filename}_bright.jpg"), brightness_inc)

    # Brightness adjustment (decrease)
    brightness_dec = cv2.convertScaleAbs(image, alpha=0.8, beta=-10)
    cv2.imwrite(os.path.join(result_folder_path, f"{filename}_dark.jpg"), brightness_dec)

    # Gaussian blur
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite(os.path.join(result_folder_path, f"{filename}_blur.jpg"), blurred)

    # Zoom (center crop and resize)
    h, w = image.shape[:2]
    crop_size = int(min(h, w) * 0.75)
    start_x = (w - crop_size) // 2
    start_y = (h - crop_size) // 2
    cropped = image[start_y:start_y+crop_size, start_x:start_x+crop_size]
    zoomed = cv2.resize(cropped, (w, h), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(os.path.join(result_folder_path, f"{filename}_zoom.jpg"), zoomed)

    # Combined transformation: horizontal flip + rotation
    flip_rotate = cv2.rotate(flipped_horizontal, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(result_folder_path, f"{filename}_horizontal_rotate.jpg"), flip_rotate)


######################
#
######################
def process_dataset(input_dir: str, output_dir: str) -> None:
    """
    Desc:
        Processes all .jpg images in a directory by applying augmentations and saving results.
    Args:
        input_dir (str): Path to the directory containing input images.
        output_dir (str): Path to the directory to save augmented images.
    Returns:
        None
    """
    os.makedirs(output_dir, exist_ok=True)

    files = [f for f in os.listdir(input_dir) if f.lower().endswith(".jpg")]
    print(f"Found {len(files)} images to augment.")

    for filename in tqdm(files, desc="Augmenting images"):
        image_path = os.path.join(input_dir, filename)
        augment_img(image_path, output_dir)


######################
#
######################
if __name__ == "__main__":

    input_dir  = "path_to_input_dir"
    output_dir = "path_to_output_dir"
    
    process_dataset(input_dir, output_dir)