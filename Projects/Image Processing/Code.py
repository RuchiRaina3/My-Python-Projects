# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:05:50 2020

@author: lockd

                Image Processing
                
"""

'For Mirrored Image'
from PIL import Image

img = Image.open("Mirrored Image.png")

"""Image is stored in computer as a matrix. Now, we have to flip that image
and in computer image is actually a matrix and flipping matrix means to
transpose a matrix i.e. interchanging rows and columns"""

#Transposing
trans_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#Since trans_img is in matrix form so, save it to a file which is human readable.
trans_img.save('Corrected Image.png')

print('Done Flipping')


'Image Enhancement Using Contrast limited Adaptive Histogram Equalization (CLAHE)'
import cv2

#Read the image
img2 = cv2.imread('To Be Enhanced.jpg')

#Preperation For CLAHE
clahe = cv2.createCLAHE()

#CLAHE technique works better when image is black and white.
#So convert in Gray Scale Image
gray_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Apply Enhancement
enh_img = clahe.apply(gray_img)
#Saving Enhanced Image
cv2.imwrite('Enhanced.jpg', enh_img)

print('Done Enhancement')

