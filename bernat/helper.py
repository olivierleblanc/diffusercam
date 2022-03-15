import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
from skimage import draw
from scipy import signal
from PIL import Image


sy=10
sx=15
max_y=4
max_x=4
radi=2

disk_mask = np.ones((sy, sx), dtype=float)
rr = np.array([max_y-1, max_y-1, max_y-1, max_y, max_y, max_y, max_y+1, max_y+1, max_y+1])
cc = np.array([max_x-1, max_x, max_x+1, max_x-1, max_x, max_x+1, max_x-1, max_x, max_x+1])
disk_mask[rr, cc] = 0

plt.imshow(disk_mask,cmap='gray')
plt.grid()
plt.show()

# rr = np.array([m])
print(rr, cc)
