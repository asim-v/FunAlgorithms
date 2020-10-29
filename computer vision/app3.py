import numpy as np
import cv2
#cargamos los clasicadores requeridos
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#utilizamos la camara 1
cap = cv2.VideoCapture(0)
while(True):    
    ret, img = cap.read()#lee el objeto de la camara
    #convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #buscamos las coordenadas de los rostros
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
    #Mostramos la imagen
    cv2.imshow('img',img)
    #con la tecla ‘q’ salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
