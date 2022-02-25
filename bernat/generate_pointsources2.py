import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
from scipy import signal

def sources_f(dist,hfilter):
    sx = len(hfilter[0])
    sy = len(hfilter)
    output=np.zeros((sy,sx), dtype=int) #Generates a sy by sx null matrix
    output[math.floor(sy/2),math.ceil((sx-1)/2-dist)]=1  #Sets to 1 a position at distance -dist respect to the center
    output[math.floor(sy/2),math.floor((sx-1)/2+dist)]=1 #Sets to 1 a position at distance +dist respect to the center
    output_f = signal.convolve2d(output, hfilter, boundary='symm', mode='same')
    return output_f

# Import filter (h(t))
h = mpimg.imread('images/pic0001.jpg')
h = h[:, :, 0] #For instance, at point (100,50) we had [0.608, 0.608, 0.608]. Now only have a single 0.608 value.

d=200
out=sources_f(d,h)
print(out)
plt.imshow(out, cmap='gray')
# plt.plot(out)
plt.show()