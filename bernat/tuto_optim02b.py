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
    output=np.zeros((sy,sx), dtype=float) #Generates a sy by sx null matrix
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
h = np.array(h,dtype=float)
h = h[:, :, 0] #For instance, at point (100,50) we had [0.608, 0.608, 0.608]. Now only have a single 0.608 value.
size_x = len(h[0])
size_y = len(h)
print(h.shape) #[Y,X]
print(size_x)
print(size_y)
print('h(t) imported and reduced correctly!')


# # Import image (i0(t))
# i0 = Image.open('images/i0_0001.jpg')
# newsize=(1639,1231)
# # newsize=tuple(int(ti/factor) for ti in realsize)
# i0=i0.resize(newsize,Image.ANTIALIAS)
# i0 = np.array(i0)
# i0 = i0[:, :, 0] #For instance, at point (100,50) we had [0.608, 0.608, 0.608]. Now only have a single 0.608 value.
# print('i0(t) imported and reduced correctly!')


#####
#####
##### PART 1
#####
#####
#####


# Generate image (i0(t))
d0=10
x_0=sources_s(d0,size_x,size_y)  #We generate the possible input
i_0=signal.fftconvolve(x_0, h,mode='full') #We filter it with h(t)
print('i0(t) generated correctly!')

# Optimization
norma_min = 10000000000 #We start with a large value (10.000.000.000) that will be reemplaced by the first calculated L2 norm.
d_min_start = 1
d_min_end = 1
d_array=np.array([],dtype=float) #To make a plot, we initialize this np.array for the x-axis
norm_array=np.array([],dtype=float) #To make a plot, we initialize this np.array for the y-axis
range_d=math.floor(len(h[0])/2)
print(range_d) #We print the range to know, in advance, the number of iterations

for d in range(5,16):
    x_s=sources_s(d,size_x,size_y)  #We generate the possible input
    i_s=signal.fftconvolve(x_s, h,mode='full') #We filter it with h(t)
    norma = np.linalg.norm(i_0-i_s)
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

x_full=d_array
y_full=norm_array

plt.plot(x_full,y_full)


plt.show()


# #####
# #####
# ##### PART 2
# #####
# #####
# #####


# # Generate image (i0(t))
# d0=100
# x_0=sources_s(d0,size_x,size_y)  #We generate the possible input
# i_0=signal.fftconvolve(x_0, h,mode='valid') #We filter it with h(t)
# print('i0(t) generated correctly!')

# # Optimization
# norma_min = 10000000000 #We start with a large value (10.000.000.000) that will be reemplaced by the first calculated L2 norm.
# d_min_start = 1
# d_min_end = 1
# d_array=np.array([],dtype=float) #To make a plot, we initialize this np.array for the x-axis
# norm_array=np.array([],dtype=float) #To make a plot, we initialize this np.array for the y-axis
# range_d=math.floor(len(h[0])/2)
# print(range_d) #We print the range to know, in advance, the number of iterations

# for d in range(1,range_d):
#     x_s=sources_s(d,size_x,size_y)  #We generate the possible input
#     i_s=signal.fftconvolve(x_s, h,mode='valid') #We filter it with h(t)
#     norma = np.linalg.norm(i_0-i_s)
#     if norma<=norma_min:
#         d_min_end=d
#     if norma<norma_min:
#         norma_min=norma
#         d_min_start=d
#     print(d,d_min_start,d_min_end,norma,norma_min)
#     d_array=np.insert(d_array,len(d_array),d)
#     norm_array=np.insert(norm_array,len(norm_array),norma)
    
# i_min=math.floor((d_min_start+d_min_end)/2)
# print("d mínima = ",i_min,[d_min_start,d_min_end])

# x_valid=d_array
# y_valid=norm_array





# #####
# #####
# ##### PART 3
# #####
# #####
# #####


# # Generate image (i0(t))
# d0=100
# x_0=sources_s(d0,size_x,size_y)  #We generate the possible input
# i_0=signal.fftconvolve(x_0, h,mode='valid') #We filter it with h(t)
# print('i0(t) generated correctly!')

# # Optimization
# norma_min = 10000000000 #We start with a large value (10.000.000.000) that will be reemplaced by the first calculated L2 norm.
# d_min_start = 1
# d_min_end = 1
# d_array=np.array([],dtype=float) #To make a plot, we initialize this np.array for the x-axis
# norm_array=np.array([],dtype=float) #To make a plot, we initialize this np.array for the y-axis
# range_d=math.floor(len(h[0])/2)
# print(range_d) #We print the range to know, in advance, the number of iterations

# for d in range(1,range_d):
#     x_s=sources_s(d,size_x,size_y)  #We generate the possible input
#     i_s=signal.fftconvolve(x_s, h,mode='same') #We filter it with h(t)
#     norma = np.linalg.norm(i_0-i_s)
#     if norma<=norma_min:
#         d_min_end=d
#     if norma<norma_min:
#         norma_min=norma
#         d_min_start=d
#     print(d,d_min_start,d_min_end,norma,norma_min)
#     d_array=np.insert(d_array,len(d_array),d)
#     norm_array=np.insert(norm_array,len(norm_array),norma)
    
# i_min=math.floor((d_min_start+d_min_end)/2)
# print("d mínima = ",i_min,[d_min_start,d_min_end])

# x_same=d_array
# y_same=norm_array





# Plotting
# fig = plt.figure()

# ax = fig.add_subplot(1, 3, 1)
# plt.plot(x_full,y_full)
# plt.title('full')

# ax = fig.add_subplot(1, 3, 2)
# plt.plot(x_valid,y_valid)
# plt.title('valid')

# ax = fig.add_subplot(1, 3, 3)
# plt.plot(x_same,y_same)
# plt.title('same')

# plt.show()