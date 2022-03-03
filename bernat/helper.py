import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
from skimage import draw
from scipy import signal
from PIL import Image

depth_030 = Image.open('from_camera/test02/depth_030.png')
# realsize=depth_030.size
# factor=4
# newsize=tuple(int(ti/factor) for ti in realsize)
# depth_030=depth_030.resize(newsize,Image.ANTIALIAS)
# depth_030 = np.array(depth_030,dtype=float)
# depth_030 = depth_030[:, :, 0]

# #Get rid of the offset
# print('Mean:',depth_030.mean())
# depth_030 = depth_030 - depth_030.mean()
# print('Mean:',depth_030.mean())

# #Print size
# [size_y,size_x]=depth_030.shape
# print(depth_030.shape) #[Y,X]

# #Print image
# plt.imshow(depth_030,cmap='gray')
# plt.title('030')
# plt.show()

# #The next ones
# #Depth_040
# depth_040 = Image.open('from_camera/test02/depth_040.png')
# depth_040=depth_040.resize(newsize,Image.ANTIALIAS)
# depth_040 = np.array(depth_040,dtype=float)
# depth_040 = depth_040[:, :, 0]
# depth_040 = depth_040 - depth_040.mean()
# plt.imshow(depth_040,cmap='gray')
# plt.title('040')
# plt.show()


# def image_open_mean_show(name,new_size,colormap):
#     location='from_camera/test02/'+name+'.png'
#     image_im = Image.open(location)
#     image_im=image_im.resize(new_size,Image.ANTIALIAS)
#     image_im = np.array(image_im,dtype=float)
#     image_im = image_im[:, :, 0]
#     image_im = image_im - image_im.mean()
#     plt.imshow(image_im,cmap=colormap)
#     plt.title('image_im')
#     plt.show()
#     return image_im

# depth_041=image_open_mean_show('depth_040',newsize,'gray')