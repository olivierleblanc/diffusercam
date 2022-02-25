import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
from skimage import draw

def surface_disk(radi,sx,sy):
    arr = np.zeros((sy, sx))
    rr, cc = draw.disk(((sy-1)/2,(sx-1)/2),radi)
    arr[rr, cc] = 1
    return arr

x=surface_disk(10,100,50)
plt.imshow(x)
plt.show()