import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
img=mpimg.imread('diablos.png')
imgplot = plt.imshow(img)
plt.show()
lum_img = img[:,:,0]
plt.imshow(lum_img)
plt.show()
plt.imshow(lum_img, cmap="hot")
plt.show()
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.show()
def grey ():
    fname = 'diablos.png'
    image = Image.open(fname).convert("L")
    arr = np.asarray(image)
    plt.imshow(arr, cmap='gray')
    plt.show()
grey()