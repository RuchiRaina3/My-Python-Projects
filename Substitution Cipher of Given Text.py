# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:02:59 2020

@author: lockd

        
                    SUBSTITUTION CIPHER Of Given Text   
                

"""

import string


#For encrypting
dict1 = {}  #Dict1 to store the substitution of the letters

key = int(input("Enter key: "))

for i in range(len(string.ascii_letters)):  #I could also make a variable and store string.asci_letters in it
    dict1[string.ascii_letters[i]] = string.ascii_letters[(i+key)%len(string.ascii_letters)]
           #Key                           #Value

plain_txt = 'Hey, I am studying the encryption by Substitution Cypher'
encry_text = []

for c in plain_txt:
     if c in dict1:  #To check as plain_txt has space/symbols also
         c = dict1[c]   #I could have also used a variable, say temp in place of c
         encry_text.append(c)
     else:
         encry_text.append(c)

encry_text = ''.join(encry_text)    #To join encry_text list as a string

print('Encrypted text is: ', encry_text) 

print()


#For recovering
dict2 = {}  #Dict2 to store the substitution of the letters

for i in range(len(string.ascii_letters)):  #I could also make a variable and store string.asci_letters in it
    dict2[string.ascii_letters[i]] = string.ascii_letters[(i-key)%len(string.ascii_letters)]  #% So that for i=51, it doesn't give any error
           #Key                           #Value

recovered_text = []

for c in encry_text:
     if c in dict2:  #To check as plain_txt has space/symbols also
         c = dict2[c]   #I could have also used a variable, say temp in place of c
         recovered_text.append(c)
     else:
         recovered_text.append(c)

recovered_text = ''.join(recovered_text)   
print('Recovered Text is: ', recovered_text)
         
     
     
        
    
