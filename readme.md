# ImageCombination-Gen


![](cover.gif)


## Introduction
This Python script is designed to generate combinations of images by overlaying layers from different input images. It takes a set of input images organized in directories, combines them in all possible permutations, and saves the resulting images in an output directory.

## Requirements

To run this script, you'll need:

**Python 3**: Make sure you have Python 3 installed on your system.

**NumPy**: This script utilizes NumPy for array operations.

**Scikit-Image**: The script uses the skimage\.io module from scikit-image for image I/O operations.  

Both Numpy and Scikit-Image can be installed using your Python package manager.

## Usage
**Organize Input Images:**
Place your input images in the input directory. Organize them into subdirectories if you want to group images that should be combined together.

**Run the Script:**
Execute the script\.py script. You can run it from the command line:
`python script.py`

**View Output:**
The script will generate all possible combinations of images and save them in the output directory.

## Additional Notes
- Make sure your input images are the same shape and in PNG format.
- The script combines images in a way that the images from the last layers will be on top of the images from the earlier layers.
- For a better understanding of how to organize your input images, take a look at the example folder in the repository.
- Depending on the number and size of input images, the script may take some time to execute, especially for a large number of combinations.
