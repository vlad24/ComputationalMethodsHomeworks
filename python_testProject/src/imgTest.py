import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('mercedes.jpg',0)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# 
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# 
# for i in xrange(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# 
# plt.show()

#########################################################

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('mercedes.jpg')
#gives an array of the desired datatype filled with one
kernel = np.float32([[1,0,1],[1,1,-4], [1,0,-1]])
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow('qq',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 
# img2 = cv2.imread('j.png',0)
# kernel2 = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img2,kernel2,iterations = 1)
# opening = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel2)
# cv2.imshow('tt', opening)
# 
# cv2.waitKey(0)
# cv2.destroyAllWindows()
