# exploring python libraries

import pandas as pd
import numpy as np

from glob import glob

import cv2
import matplotlib.pylab as plt

files = glob('file destination')

img_mpl = plt.imread(files)

# opencv

img_cv2 = cv2.imread(files)
# img_cv2.shape - height, width, channels (usually 3 - rgb)

# displaying an image using matplotlib
fig, ax = plt.suplots(figsize=(10,10))
ax.imshow(img_mpl)

# showing rgb channels - matplotlib

fig, axs = plt.subplots(1,3, figsize=(15,5))
axs[0].imshow(img_mpl[:,:,0], cmap='Reds')
axs[1].imshow(img_mpl[:,:,1], cmap='Greens')
axs[2].imshow(img_mpl[:,:,2], cmap='Blues')

axs[0].axis('off')
axs[1].axis('off')
axs[2].axis('off')

axs[0].set_title('Red channel')
axs[1].set_title('Green channel')
axs[2].set_title('Blue channel')

plt.show()

# cv2 reads in BGR (Blue, Green, Red)

fig, axs = plt.subplots(1,2,figsize=(10, 5))

axs[0].imshow(img_cv2)
axs[0].axis('off')
axs[1].imshow(img_mpl)
axs[1].axis('off')

plt.show

# convert from BGR to RGB

cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)

# image manipulation

img = plt.imread(files)

fig, ax = plt.subplots(figsize=(8,8))
ax.imshow(img)
ax.axis('off')
plt.show()

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_gray.shape # will only have a height and width as gray scale is only one channel. e.g. (485, 596)

# resizing and scaling

img_shrunk = cv2.resize(img, None, fx=0.25, fy=0.25)
# the image is being shrunk to 0.25 of its original value.

img_resize = cv2.resize(img, (100,100)) 

# numpy
# sharpening and blurring

# cv2 kernals

kernel_sharpening = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])

kernel_3x3 = np.ones((3,3), np.float32) / 9

sharpened_img = cv2.filter2D(img, -1, kernel_sharpening)
blurred_img = cv2.filter2D(img, -1, kernel_3x3)



# Scikit-learn


# tensorflow

