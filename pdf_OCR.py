import pytesseract
from pdf2image import convert_from_path
import os

pytesseract.pytesseract.tesseract_cmd = "C:\\projects\\dependencies\\Tesseract-OCR\\tesseract.exe"
popplerPath = "C:\\projects\\dependencies\\poppler-22.01.0\\Library\\bin"

def pdf_ocr(DIR, LANG):
    """
    performs OCR on a given directory of pdf files
    :param DIR: string of directory with pdf files
    :param LANG: string of language for text recognition
    :return: none. new textfiles created in given directory
    """
    files = os.listdir(DIR)
    for file in files:
        if file.endswith("pdf"):
            #strip file extension to get string of filename
            filename = file[:-4]
            # if pdf has not been converted already
            if "{}.txt".format(filename) not in files:
                #convert to list of image files
                images = convert_from_path(DIR+file, 350, poppler_path=popplerPath)
                with open("{}\\{}.txt".format(DIR, filename), 'a') as f:
                    # ocr each image in list
                    for image in images:
                        text = (str(pytesseract.image_to_string(image, lang=LANG)))
                        f.write(text)