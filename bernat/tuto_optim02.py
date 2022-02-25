import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
from scipy import signal
from PIL import Image

# Define function to minimize
def sources_s(dist,sx,sy):
    # sx = len(hfilter[0])
    # sy = len(hfilter)
    output=np.zeros((sy,sx), dtype=int) #Generates a sy by sx null matrix
    output[math.floor(sy/2),math.ceil((sx-1)/2-dist)]=1  #Sets to 1 a position at distance -dist respect to the center
    output[math.floor(sy/2),math.floor((sx-1)/2+dist)]=1 #Sets to 1 a position at distance +dist respect to the center
    return output

# # Import filter (h(t))
# h = mpimg.imread('images/pic0001.jpg')
# h = h[:, :, 0] #For instance, at point (100,50) we had [0.608, 0.608, 0.608]. Now only have a single 0.608 value.
# size_x = len(h[0])
# size_y = len(h)
# print(h.shape)  #[Y,X]


# Import filter (h(t))
h = Image.open('images/h_0001.jpg')
realsize=h.size
print(realsize)
factor=4
newsize=tuple(int(ti/factor) for ti in realsize)
print(newsize)
h=h.resize(newsize,Image.ANTIALIAS)
h = np.array(h)
h = h[:, :, 0] #For instance, at point (100,50) we had [0.608, 0.608, 0.608]. Now only have a single 0.608 value.
size_x = len(h[0])
size_y = len(h)
print(h.shape) #[Y,X]
print(size_x)
print(size_y)
print('h(t) imported and reduced correctly!')


# Import image (i0(t))
i0 = Image.open('images/i0_0001.jpg')
newsize=(1639,1231)
# newsize=tuple(int(ti/factor) for ti in realsize)
i0=i0.resize(newsize,Image.ANTIALIAS)
i0 = np.array(i0)
i0 = i0[:, :, 0] #For instance, at point (100,50) we had [0.608, 0.608, 0.608]. Now only have a single 0.608 value.
print('i0(t) imported and reduced correctly!')

# Optimization
norma_min = 10000000000 #We start with a large value (10.000.000.000) that will be reemplaced by the first calculated L2 norm.
d_min_start = 1
d_min_end = 1
d_array=np.array([],dtype=float) #To make a plot, we initialize this np.array for the x-axis
norm_array=np.array([],dtype=float) #To make a plot, we initialize this np.array for the y-axis
range_d=math.floor(len(h[0])/2)
print(range_d) #We print the range to know, in advance, the number of iterations

for d in range(1,range_d):
    x_s=sources_s(d,size_x,size_y)  #We generate the possible input
    i_s=signal.fftconvolve(x_s, h,mode='full') #We filter it with h(t)
    norma = np.linalg.norm(i0-i_s)
    if norma<=norma_min:
        d_min_end=d
    if norma<norma_min:
        norma_min=norma
        d_min_start=d
    print(d,d_min_start,d_min_end,norma,norma_min)
    d_array=np.insert(d_array,len(d_array),d)
    norm_array=np.insert(norm_array,len(norm_array),norma)
    
i_min=math.floor((d_min_start+d_min_end)/2)
print("d mínima = ",i_min,[d_min_start,d_min_end])


plt.plot(d_array,norm_array)
plt.ylabel('norm')
plt.xlabel('d')
plt.title('optimization')
plt.show()


# Plotting
# fig = plt.figure()

# ax = fig.add_subplot(1, 2, 1)
# plt.imshow(x0, cmap='gray')
# plt.title('x0(t)')

# ax = fig.add_subplot(1, 2, 2)
# plt.imshow(xs, cmap='gray')
# plt.title('xs(t)')

# plt.show()