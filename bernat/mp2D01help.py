import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
from skimage import draw
from scipy import signal
from PIL import Image

[h_auto_y,h_auto_x]=[270,480]

np.random.seed(1)
x=np.zeros((h_auto_y,h_auto_x),dtype=float)
k=10
random_x=(np.random.rand(k)*h_auto_x*1.2).astype(int)
random_y=(np.random.rand(k)*h_auto_y).astype(int)
x[random_y,random_x]=1
print(random_y)
print(random_x)
plt.imshow(x,cmap='gray')
plt.show()