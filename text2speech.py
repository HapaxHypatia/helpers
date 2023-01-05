# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:17:00 2021

@author: Bec
"""
import site
def text2speech(string, LANG):

    # site.addsitedir('C:\\Program Files\\Python311\\Lib\\site-packages')
    from gtts import gTTS
    tts = gTTS(string, lang=LANG)
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tempdir:
        print(tempdir)
        path = tempdir + '\\'+string + ".mp3"
        tts.save(path)
        print(path)
    return path
    # import acoustid
    # fprint = acoustid.fingerprint_file(path)
    # return fprint


text2speech("bonjour", "fr")
        