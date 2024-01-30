#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crypto.Cipher import Salsa20

ctext1 = b'1U\xe0N\xb6\x8c\x19<H\xac\x1f]bm\x0f\xe8\xe9z\xfe*\xad\xaa\x8e@\x81\x8fE\xcfBe\xd0\x96\xe0\x08t\xef\t\x9bg(\x86`/ 8_\xcc\xdbF\xde\x13w\xb1e\xec\x92Au\xfd\xea\xbeU\xf1\xda \xb1\xc5D\xb1\xf9\x9as\xd9?{z \x90R[\xee\xe0XLv=\xd9\x10jN\xdc\x87\x82\xdfO%Z\xb7P'
ctext2 = b'N\x0e\xb6^\xccU\xe0\x8b\x1e4\r\xbd\x1eJc|\x03\xb8\xe8|\xfd,\xb0\xb2\x8bK\xc6\xc6_\x81U\x7f\xd4\x86\xa9\x13w\xff\t\x9fa{\x85!(;%\x11\xcd\x94]\xdd\x13l\xbb0\xf5\x8fKn\xf5\xe4'
ctext3 = b'\xccU\xe0N\x0e\xb6^1\x99\x1fy\r\xb2\x06Jcm\x0f\xf1\xe83\xf1i\xb4\xbf\x90V\xce\x88\x16\x98^b\x91\x8a\xa1\x02;\xf7H\x92w{\x93,-o8\x17\xcf\x94D\xdb@z\xbf{\xfb\x92\x04m\xf3\xab\xab\x1b\xf6\x9b7\xfe\xd2\x01\xf0\xe6\x9e7\xc8ww4e\x90\x01D\xee\xe1ULh9\xd9\x11jW\xdc\x95\x84\x9aE.\x1b'
ctexts = [ctext1, ctext2, ctext3]

secret = 14192977154127950076
key = secret.to_bytes(32, byteorder='big')

for i in range(len(ctexts)):
    try:
        ctext_nonce = ctexts[i][:8]
        ciphertext = ctexts[i][8:]
        cipher = Salsa20.new(key, nonce=ctext_nonce)
        dtext = cipher.decrypt(ciphertext)
        dtext.decode('UTF-8')
        print("The correct nonce belongs to ctext"+str(i+1))
        #The correct nonce belongs to ctext3
    except:
        continue
        
for i in range(len(ctexts)):
    for j in range(9):
        try:
            ciphertext = ctexts[i][j:]
            cipher = Salsa20.new(key, nonce=ctext_nonce)
            dtext = cipher.decrypt(ciphertext)
            print("Decoded ctext"+str(i+1)+": ", dtext.decode('UTF-8'))
            #Decoded ctext1:  The first principle is that you must not fool yourself and you are the easiest person to fool.
            #Decoded ctext2:  Somewhere, something incredible is waiting to be known.
            #Decoded ctext3:  An expert is a person who has made all the mistakes that can be made in a very narrow field.
        except:
            continue

