# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:17:00 2021

@author: Bec
"""
   
def text2speech(string):
    import site
    site.addsitedir('C:\\Users\\rebecca.haskmann\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages')
    from gtts import gTTS
    tts = gTTS(string, lang="en")
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tempdir:
        print(tempdir)
        path = tempdir + '\\'+string + ".mp3"
        tts.save(path)
        import acoustid
        fprint = acoustid.fingerprint_file(path)
        return fprint


        
        