# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
# import math
# from skimage import draw
# from scipy import signal
# from PIL import Image


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math


x = np.linspace(-40,40, 40)
new_x = np.array([[]],dtype=float)
for i in range(40):
    new_x = np.append(new_x,[[stats.norm.pdf(x, 0,10)[i]]],axis = 1)

plt.imshow(new_x)
plt.show()
plt.plot(range(40),new_x[0,:])
plt.show()
print(new_x)

# mu = 0
# sigma = 100
# x = np.linspace(mu - 3*sigma, mu + 3*sigma, 40)
# new_x = np.array([[]],dtype=float)
# for i in range(40):
#     new_x = np.append(new_x,[[stats.norm.pdf(x, mu, sigma)[i]]],axis = 1)

# plt.imshow(new_x)
# plt.show()
# plt.plot(range(40),new_x[0,:])
# plt.show()
# print(new_x)