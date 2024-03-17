import cv2
import os 
import time
image = cv2.imread("saca_1.jpg")
nm = "fala_dele.jpg"
nm2 = "oi"
###cv2.imshow(nm2,image) exibir a imagem em uma janela
image_cinza = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_, image_binary = cv2.threshold(image_cinza, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
image_final = cv2.GaussianBlur(image_cinza, (3, 3), 0)
cv2.imwrite(nm, image_final)
print(nm)