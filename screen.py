
from PIL import Image
import pytesseract


def stringtotext():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    dosyaadi = input("Dosya Adını Giriniz: ")
    a=pytesseract.image_to_string(Image.open('{}'.format(dosyaadi)), lang="tur")

    wr = open("yazi.doc", "w+")
    wr.write(a)
    wr.close()