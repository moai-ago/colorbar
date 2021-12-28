import numpy as np
import tifffile as tiff
import os


gradient = np.arange(255)
gray_bar = np.tile(gradient,(10,1))

script_dir = os.path.dirname(__file__)

gray_w = script_dir + "\\colorbar.tif"

tiff.imsave(gray_w, gray_bar, photometric="minisblack")
