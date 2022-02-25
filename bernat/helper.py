import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
from scipy import signal
from PIL import Image

# Import filter (h(t))
h = mpimg.imread('images/pic0001.jpg')
h = h[:, :, 0] #For instance, at point (100,50) we had [0.608, 0.608, 0.608]. Now only have a single 0.608 value.
size_x = len(h[0])
size_y = len(h)
print(h.shape)  #[Y,X]
print(h)