import os 
from os                         import listdir
from numpy                      import asarray
from datetime                   import datetime
from pix2pix_cgan               import define_discriminator, define_generator, define_gan, train
from keras.preprocessing.image  import img_to_array
from keras.preprocessing.image  import load_img


# load all images in a directory into memory
def load_images(path, size=(256, 512)):
    src_list, tar_list = list(), list()
    # enumerate filenames in directory, assume all are images
    for filename in listdir(path):
        # load and resize the image
        pixels = load_img(os.path.join(path, filename), target_size=size)
        # convert to numpy array
        pixels = img_to_array(pixels)
        # split into satellite and map
        sat_img, map_img = pixels[:, :256], pixels[:, 256:]
        src_list.append(sat_img)
        tar_list.append(map_img)
    return [asarray(src_list), asarray(tar_list)]


# dataset path
path = "path_to_train_dir"

# load dataset
[src_images, tar_images] = load_images(path)
print("Loaded: ", src_images.shape, tar_images.shape)

# define input shape based on the loaded dataset
image_shape = src_images.shape[1:]

# define the models
d_model = define_discriminator(image_shape)
g_model = define_generator(image_shape)
# define the composite model
gan_model = define_gan(g_model, d_model, image_shape)

# Define data
# load and prepare training images
data = [src_images, tar_images]


def preprocess_data(data):
    # load compressed arrays
    # unpack arrays
    X1, X2 = data[0], data[1]
    # scale from [0,255] to [-1,1]
    X1 = (X1 - 127.5) / 127.5
    X2 = (X2 - 127.5) / 127.5
    return [X1, X2]


dataset  = preprocess_data(data)
n_epochs = 100

start1 = datetime.now()

train(d_model, g_model, gan_model, dataset, n_epochs=n_epochs, n_batch=1)

stop1 = datetime.now()

# Execution time of the model
execution_time = stop1 - start1
print("Execution time is: ", execution_time)