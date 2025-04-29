import os
import numpy as np
from   keras.models                 import load_model
from   keras.preprocessing.image    import load_img, img_to_array
from   matplotlib                   import pyplot


######################
# Configuration
######################
RESNET_PATH    = "path_to_resnet50_model.h5"
CGAN_PATH      = "path_to_cgan_model.h5"

DATA_PATH      = "path_to_test_dir"
OUTPUT_PATH    = "path_to_output_dir"

HEIGHT, WIDTH  = 256, 256
TARGET_SIZE    = (HEIGHT, WIDTH)
BATCH_SIZE     = 32

os.makedirs(OUTPUT_PATH, exist_ok=True)


# Load the models
resnet_model = load_model(RESNET_PATH)
print("Resnet50 loaded successfully!")

cgan_model = load_model(CGAN_PATH)
print("cGAN loaded successfully!")


######################
#
######################
def load_and_preprocess(img_path: str, model: str = "resnet") -> np.ndarray:
    """
    Desc:
        Load an image from disk and preprocess it for input into a deep learning model.
    Args:
        img_path (str): Path to the image file.
        model (str): The model type to preprocess for. 
                     "resnet" uses scaling to [0,1], other models use [-1,1] normalization.
    Returns:
        np.ndarray: Preprocessed image ready for model input.
    """
    img = load_img(img_path, target_size=TARGET_SIZE)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    if model == "resnet":
        return img_array / 255.0
    return (img_array - 127.5) / 127.5
    

######################
#
######################
def plot_generated_image(gen_image: np.ndarray, filename: str) -> None:
    """
    Save a generated image to disk after rescaling it from [-1, 1] to [0, 1].
    Args:
        gen_image (np.ndarray): The generated image array, expected shape (1, H, W, C).
        filename (str): The filename to save the image as (including extension, e.g., "image.png").
    Returns:
        None
    """
    # Scale from [-1,1] to [0,1]
    gen_image = (gen_image + 1) / 2.0

    # Save the generated image
    output_filename = os.path.join(OUTPUT_PATH, filename)
    pyplot.imsave(output_filename, gen_image[0])


all_ctr    = 0
spiral_ctr = 0

# === Loop through images ===
for filename in os.listdir(DATA_PATH):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    img_path = os.path.join(DATA_PATH, filename)
    all_ctr += 1

    # Step 1: Classify with ResNet50
    resnet_input = load_and_preprocess(img_path)
    resnet_preds = resnet_model.predict(resnet_input, verbose=0)

    predicted_class = np.argmax(resnet_preds, axis=1)[0]
    if predicted_class == 1:  # Spiral galaxy

        if resnet_preds[0][1] > 0.65:    # Confidence threshold

            # Step 2: Process with cGAN
            cgan_input  = load_and_preprocess(img_path, "cgan")
            cgan_output = cgan_model.predict(cgan_input, verbose=0)
            plot_generated_image(cgan_output, filename)
            spiral_ctr += 1

    print(f"Found '{spiral_ctr}' spiral galaxies in '{all_ctr}' images.")  