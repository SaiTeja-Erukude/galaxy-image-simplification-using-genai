import os
from   PIL        import Image
from   tqdm       import tqdm


######################
#
######################
def concatenate_images(image1_path: str, image2_path: str, output_path: str) -> bool:
    """
    Desc:
        Concatenates two images side-by-side (horizontally) and saves the result to a specified path.
    Parameters:
        image1_path (str): File path to the first image (will appear on the left).
        image2_path (str): File path to the second image (will appear on the right).
        output_path (str): File path where the resulting concatenated image will be saved.
    Returns:
        bool: True if the images were successfully concatenated and saved, False if an error occurred.
    """
    try:
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)
        
        width1, height1 = image1.size
        width2, height2 = image2.size
        
        if height1 != height2:
            print(f"Images have different heights. Cannot concatenate: {image1_path}, {image2_path}")
            return False
        
        collage_width = width1 + width2
        collage_height = height1
        
        collage = Image.new("RGB", (collage_width, collage_height))
        collage.paste(image1, (0, 0))
        collage.paste(image2, (width1, 0))
        
        collage.save(output_path)
        return True

    except Exception as concat_ex:
        print(f"Error occurred while concatenating: {concat_ex}")
        return False
    

######################
#
######################
if __name__ == "__main__":
    
    original_images  = "path_to_input_dir"    
    annotated_images = "path_to_annotated_dir"
    output_path      = "path_to_output_dir"
    
    # Make sure output directory exists
    os.makedirs(output_path, exist_ok=True)
    
    for filename in tqdm(os.listdir(original_images)):
        if filename.lower().endswith((".jpg", ".jpeg")):
            original_image_path  = os.path.join(original_images, filename)
            annotated_image_path = os.path.join(annotated_images, filename)
            output_image_path    = os.path.join(output_path, filename)
            
            # Check if both files exist
            if os.path.exists(annotated_image_path):
                concatenate_images(original_image_path, 
                                  annotated_image_path, 
                                  output_image_path)