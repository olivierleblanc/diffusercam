import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

def sources(dist):
    sx = 600   
    sy = 400
    output=np.zeros((sy,sx), dtype=int) #Generates a sy by sx null matrix
    output[math.floor(sy/2),math.ceil((sx-1)/2-dist)]=1  #Sets to 1 a position at distance -dist respect to the center
    output[math.floor(sy/2),math.floor((sx-1)/2+dist)]=1 #Sets to 1 a position at distance +dist respect to the center
    return output

out=sources(200)
print(out)
plt.imshow(out, cmap='gray')
# plt.plot(out)
plt.show()