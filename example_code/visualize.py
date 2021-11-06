#dependencies required; pydicom, matplotlib, numpy

#imports
import pydicom
from pydicom.pixel_data_handlers.util import apply_color_lut
from pydicom import dcmread
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#grab the pixel array data from the dcm
fname = "Image-105.dcm" #insert your relative dcm file
ds = dcmread(fname)
arr = ds.pixel_array

#interpolate the nd.array storing the pixel array as an image and display on screen
plt.imshow(arr, interpolation='nearest')
plt.show()
