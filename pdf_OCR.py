import pytesseract
from pdf2image import convert_from_path
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
popplerPath = "C:\\projects\\VocabGrabber\\poppler-22.01.0\\Library\\bin"


def pdf_ocr(DIR, LANG):
    """
    performs OCR on a given directory of pdf files
    :param DIR: string of directory with pdf files
    :param LANG: string of language for text recognition
    :return: none. new textfiles created in given directory
    """
    for filename in os.listdir(DIR):
        images = convert_from_path(DIR+filename, 350, poppler_path=popplerPath)
        with open("{}txt".format(filename[:-3]), 'a') as f:
            for image in images:
                text = (str(pytesseract.image_to_string(image, lang=LANG)))
                f.write(text)
