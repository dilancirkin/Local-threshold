# -*- coding: utf-8 -*-
"""Dilan_Cirkin_170205009.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uWM0uFtiMxCNgXI-8F1TCka4Q-RHkuti
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("bw.png",0)
img2=img.copy()
h=img2.shape[0]
w=img2.shape[1]

img2[0:h,0:w]=img
widthParca=3
heightParca=2

for ih in range(heightParca):
    for iw in range(widthParca):
        
        x=int(w/widthParca*iw)
        y=int(h/heightParca*ih)
        hY=int(h/heightParca)
        wY=int(w/widthParca)
        roi=img2[y:y+hY,x:x+wY]
        ret,th=cv2.threshold(roi,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        img2[y:y+hY,x:x+wY]=th
        if(y<=h):
             y=y+hY
        else:
            break
    if(x<w):
            x=x+wY
    else:
        break
ret1,th1=cv2.threshold(img.copy(),127,255,cv2.THRESH_BINARY)
ret2,th2=cv2.threshold(img.copy(),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret3,th3=cv2.threshold(th,127,255,cv2.THRESH_BINARY)
titles=["Original","Global Threshold","Otsu","My Threshold"]
images=[img,th1,th2,img2]

plt.figure(figsize=(20,20))
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()



