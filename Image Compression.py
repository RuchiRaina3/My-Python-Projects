# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:14:38 2020

@author: lockd

I am compressing Image of Lena(Swedsish Model whose one image is used as a standard image for testing since 1973)

"""

import numpy as np
from PIL import Image

i1 = Image.open('Lena.jpg') #Stored Lena in i1
#i1.show() shows image or writting i1 in console also shows image
#print(i1) printed <PIL.JpegImagePlugin.JpegImageFile image mode=L size=512x512 at 0x16732280388>
pixelMap1 = i1.load()     
#print(pixelMap) prints <PixelAccess object at 0x00000167322C0D30>
I1 = np.asanyarray(i1) #Creates array of image i1 or I1 = np.asanarray(Image.open('Lena.jpg'))
print(I1) #Shows the I1 of pixel values as elements

i2 = Image.new(i1.mode, i1.size) #mode is grayscale as of i1 and size is also as of i1 and creates 
#an image of black colour as I haven't specified the colour
pixelMap2 = i2.load()
I2 = np.asanyarray(i2)
#print(I2) #All elements are 0 as i2 is of black colour

'''
  Now, 0-255 = 0-2^8. So we need 8 bits to store
  255. Now, for data compression we will map 
  2^8 - 2^3
  For that divide 2^8 with 2^3, we get 2^5. This means
      0-31    = 0
      32-63   = 1
      64-95   = 2
      96-127  = 3
      128-159 = 4
      160-191 = 5
      192-223 = 6
      224-255 = 7
'''

#i1.size[0] returns the no. of rows of i1, here, 512
#i1.size[1] returns the no. of columns of i1, here, 512
for i in range(i1.size[0]):
    for j in range(i1.size[1]):
       
        if(pixelMap1[i,j]>=0 and pixelMap1[i,j]<=31):
            pixelMap2[i,j] = 0
         
        elif(pixelMap1[i,j]>=32 and pixelMap1[i,j]<=63):
            pixelMap2[i,j] = 1
    
        elif(pixelMap1[i,j]>=64 and pixelMap1[i,j]<=95):
            pixelMap2[i,j] = 2
        
        elif(pixelMap1[i,j]>=96 and pixelMap1[i,j]<=127):
            pixelMap2[i,j] = 3
        
        elif(pixelMap1[i,j]>=128 and pixelMap1[i,j]<=159):
            pixelMap2[i,j] = 4
            
        elif(pixelMap1[i,j]>=160 and pixelMap1[i,j]<=191):
            pixelMap2[i,j] = 5
            
        elif(pixelMap1[i,j]>=192 and pixelMap1[i,j]<=223):
            pixelMap2[i,j] = 6    
            
        elif(pixelMap1[i,j]>=224 and pixelMap1[i,j]<=255):
            pixelMap2[i,j] = 7
            
i2.save('Lena2.jpg')  #Saves i2 as Lena2
I2 = np.asanyarray(i2)
print(I2)