"""
File: stanCodoshop.py
Name: Yi-Ju Lu
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # initialize rgb is 0
    red = 0
    green = 0
    blue = 0
    # to sum rgb
    for i in range(len(pixels)):
        red += pixels[i].red
        green += pixels[i].green
        blue += pixels[i].blue
    # avg rgb
    red = red//len(pixels)
    green = green//len(pixels)
    blue = blue//len(pixels)
    pixels_list = [red, green, blue]  # add to list
    return pixels_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    pixels_list_avg = get_average(pixels)  # to get avg pixel
    smallest_distance = float('inf')       # initialize the smallest distance as infinite number
    best_pixels = pixels[0]                # set best pixel
    for pixel in pixels:
        color_distance = get_pixel_dist(pixel, pixels_list_avg[0], pixels_list_avg[1], pixels_list_avg[2])
        # to determine the smallest distance, the smallest color distance is the best pixel
        if color_distance < smallest_distance:
            smallest_distance = color_distance
            best_pixels = pixel
    return best_pixels


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    #  nested for loop to get the pixel in images
    for x in range(result.width):
        for y in range(result.height):
            img_list = []  # set a list to add pixel
            for pixel in images:  # use for each loop to get pixel
                img = pixel.get_pixel(x, y)
                img_list.append(img)
            new_img = get_best_pixel(img_list)  # to get the best image
            result.get_pixel(x, y).red = new_img.red  # add best img to blank image
            result.get_pixel(x, y).green = new_img.green
            result.get_pixel(x, y).blue = new_img.blue

    # Write code to populate image and create the 'ghost' effect
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
