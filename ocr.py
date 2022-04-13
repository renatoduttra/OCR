import pytesseract
import cv2
#pip install opencv-pythonpip install opencv-python
#https://github.com/UB-Mannheim/tesseract/wiki

imagem = cv2.imread("email.JPG")

caminho = r"C:\Users\Python\AppData\Local\Programs\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem, lang="por") #
print(texto)