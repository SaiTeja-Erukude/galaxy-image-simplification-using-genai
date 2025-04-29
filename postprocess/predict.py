import os
import numpy                        as np
from   keras.models                 import load_model
from   keras.preprocessing.image    import load_img
from   keras.preprocessing.image    import img_to_array
from   numpy                        import vstack
from   matplotlib                   import pyplot
from   tqdm                         import tqdm


# plot source, generated and target images
def plot_images(src_img, gen_img, filename):
    images = vstack((src_img, gen_img))
    # scale from [-1,1] to [0,1]
    images = (images + 1) / 2.0
    titles = ["Source", "Generated"]
    # plot images row by row
    for i in range(len(images)):
        # define subplot
        pyplot.subplot(1, 2, 1 + i)
        # turn off axis
        pyplot.axis("off")
        # plot raw pixel data
        pyplot.imshow(images[i])
        # show title
        pyplot.title(titles[i])
    filename = filename.split(".")[0] + ".png"
    pyplot.savefig(os.path.join(output_dir, filename))
    print("Saved: ", filename)


# plot just the generated images
def plot_generated_images(gen_image, filename):
    # Scale from [-1,1] to [0,1]
    gen_image = (gen_image + 1) / 2.0
    
    # Save the generated image
    output_filename = os.path.join(output_dir, filename)
    pyplot.imsave(output_filename, gen_image[0])


if __name__ == "__main__":
    n_iterations = 5
    test_dir    = "path_to_test_dir"
    output_dir  = "path_to_input_dir"
    model_path  = "path_to_cgan_model.h5"

    model = load_model(model_path)

    os.makedirs(output_dir, exist_ok=True)

    size = (256, 256)
    for filename in tqdm(os.listdir(test_dir)):
        # load and resize the image
        img = load_img(os.path.join(test_dir, filename), target_size=size)
        
        # convert to numpy array
        src_image = img_to_array(img)
        src_image = np.expand_dims(src_image, axis=0)

        # scale from [0,255] to [-1,1]
        src_image = (src_image - 127.5) / 127.5

        # Iteratively apply the model n_iterations times
        current_img = src_image
        for i in range(n_iterations):
            current_img = model.predict(current_img, verbose=0)
        
        plot_generated_images(current_img, filename)