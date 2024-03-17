import cv2
import pytesseract
import pandas as pd
def clear_lista(lista):
    lista_sem_strings_vazias = [item for item in lista if bool(item.strip())]
    lista = lista_sem_strings_vazias
    return lista
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
pct_saca = []
saca = cv2.imread('saca_1.jpg')
resultado = pytesseract.image_to_string(saca)
resultado = resultado.upper()
resultado = resultado.replace('COM HORARIO COMERCIAL','')
resultado = resultado.replace('\n','')
resultado = resultado.replace(' ','')
resultado =  resultado.split("VOUPARALA")
for x in resultado:
    parada = x.split(",")
    for clear in parada:
        if clear == '' or clear == ' ':
            parada.remove(clear)
   ### parada_verif = parada[0]
    ###parada_verif = parada_verif.upper()
    ###if "COM HORARIO COMERCIAL" in parada_verif:
    ###   z = parada_verif
    ###   z = z.replace('COM HORARIO COMERCIAL','')
    ###   parada.pop(0)
    ###   parada.insert(0,z)
    ###parada_verif2 = parada[2]
    ###parada_verif2 = parada_verif2.upper()
   ### if "CEP 06" in parada_verif2:
    ###   print(parada_verif2)
   ###    z = parada_verifwaw
    ###   z = z.split('06')
       ###z = z +'\n'
       ###parada.pop(0)
       ###parada.insert(0,z)
    print(parada)
    if len(parada) > 1:
       etiqueta = parada[2]
       l_etiqueta = etiqueta.split("ENTREGA")
       print(l_etiqueta)
       l_etiqueta = clear_lista(l_etiqueta) 
       n_etiqueta = l_etiqueta[1]
       n_etiqueta = n_etiqueta.split("-")
       n_etiqueta = n_etiqueta[1]
       qtd_etiqueta = l_etiqueta[1]
       qtd_etiqueta = qtd_etiqueta[0]
       qtd_etiqueta = int(qtd_etiqueta) 
       for _ in range(qtd_etiqueta):
        pct_saca.append(n_etiqueta)

print(pct_saca)
print(len(pct_saca))

df = pd.DataFrame({'Pacotes': pct_saca})
###df = pd.DataFrame({f'Total {len(pct_saca)}': []})
df[f'Total {len(pct_saca)}'] = ''
df.to_excel('Saca.xlsx', index=False)
















### https://github.com/UB-Mannheim/tesseract/wiki
### pip install opencv-python
### pip install pytesseract