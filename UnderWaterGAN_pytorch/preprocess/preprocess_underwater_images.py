import cv2
import math
import os
from util.util import assure_path_exists

def resize_image(image, width=None, height=None):
    """ This function resizes images to a given width and height
    using opencv

    Args:
        image: input image read with cv2.imread
        width: width to resize. Defaults to None.
        height: height to resize. Defaults to None.

    Returns:
        image: resized image
    """

    dim=None
    (h,w) = image.shape[:2]
    if width is None and height is None:
        return image
    
    elif width is not None and height is not None:
        dim = (width, height)
    
    elif width is None:
        r = height/float(h)
        dim = (int(w*r), height)
    else:
        r = width / float(w)
        dim = (width, int(h*r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized


if __name__ == '__main__':
    # width and height for image resizing
    new_size_x = 1024
    new_size_y = 1024
    input_dir = "images/"
    # path to output
    output_dir = "resized_images/"
    print(output_dir)
    assure_path_exists(output_dir)

    # go through each image in directory
    for filename in os.listdir(input_dir):
        # read image
        img = cv2.imread(os.path.join(input_dir, filename))
        if img is not None:
            # resize image
            img_resized = resize_image(img, new_size_x, new_size_y)
            
            new_path = output_dir + filename
            cv2.imwrite(new_path, img_resized)
        