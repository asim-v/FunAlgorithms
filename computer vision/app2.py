import cv2
import numpy as np

img=cv2.imread('uno.jpg')

img #despliega el arreglo
img.ndim #da el numero de dimensiones
cv2.imshow('original', img)
a=img-1
img[:,:,0]=img[:,:,0]-20
cv2.imshow('modificada', img)
cv2.imshow('incrementada', a)


cv2.waitKey()
cv2.destroyAllWindows()
x