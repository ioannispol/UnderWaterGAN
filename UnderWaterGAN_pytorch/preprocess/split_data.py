import shutil
import os

import random
from tqdm import tqdm

def make_directories(root_dir):
    
    os.chdir(root_dir)
    try:
        os.makedirs('train/')
        os.makedirs(root_dir + 'val/')
        os.makedirs('test/')
        print("The directories created")
    except:
        print("The directories already exist.")

def copy_images(src, dst_train, dst_test, ratio_train=.8, ratio_test=0.2):

    # list all the files in the images main directory
    files = [f for f in os.listdir(src) if f.endswith('.jpg')]

    # select a radom percentage of images
    random_train_images = random.sample(files, int(len(files) * ratio_train))
    random_test_images = random.sample(files, int(len(files) * ratio_test))
    #train_images = [train for train in os.listdir(src)]

    # move the random images to test directory
    for i in random_test_images:
        tqdm(os.rename(src + '/' + i, dst_test + '/' + i))
        continue

    for j in os.listdir(src):
        tqdm(os.rename(src + '/' + j, dst_train + '/' + j))
        continue

    print("All files moved.")


if __name__ == '__main__':
    root_dir = os.path.normpath("D:\giann\Documents\Machine_learning\PhD_project\Dataset\custom_dataset\\")
    make_directories(root_dir)

    src = os.path.normpath("D:\giann\Documents\Machine_learning\PhD_project\Dataset\custom_dataset\main_dataset")
    dst_train = os.path.normpath("D:\giann\Documents\Machine_learning\PhD_project\Dataset\custom_dataset\\train")
    dst_test = os.path.normpath("D:\giann\Documents\Machine_learning\PhD_project\Dataset\custom_dataset\\test")
    copy_images(src, dst_train, dst_test)



