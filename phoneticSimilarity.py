# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 06:35:30 2021

@author: Bec
"""

from pyjarowinkler import distance

def phonsim (string1, string2):
    
    '''
    Compares the similarity of two strings based on consonants, length, and first letter
    
    Parameters
    ----------
    string1 : string of 1 word
    string2 : string of 1 word

    Returns
    -------
    similarity index as float.

    '''

   
    string1 = string1.lower()
    string2 = string2.lower()
    
    #remove double letters
    string1 = "".join(dict.fromkeys(string1))
    string2 = "".join(dict.fromkeys(string2))
    
    #remove vowels             
    string1 = string1[0] + remove_vowels(string1[1:])
    string2 = string2[0] + remove_vowels(string2[1:])
    
    return distance.get_jaro_distance(string1, string2, winkler=False, scaling=0.1)




def remove_vowels(string):
    vowels = "aeiou"
    result = string[:]
    #replace vocalic y
    for i in range(1, len(string)):
        if string[i]=='y':
            if i==len(string)-1: #if final
                continue
            elif string[i-1] in vowels and string[i+1] in vowels: #if intervocalic
                continue
            else:
                result = result.replace(string[i],"")
    
    for i in range(len(string)):
        if string[i] == 'i':
            try: 
                #preserve consonantal i
                if string[i-1] in vowels and string[i+1] in vowels:
                    continue
                else:
                     result = result.replace(string[i],"") 
            except IndexError:
                continue #currently skipping initial or final i. Problem?
        if string[i] in vowels:
            result = result.replace(string[i],"") 
    return result