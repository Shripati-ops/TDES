from pyDes import *
def TDES_encrypt(Image):

    #Try catch block to maintain the efficiency
    try:
        #Open the image from the file explorer

        fin = open(Image,'rb')
        img = fin.read()
        key = des("DESCRYPT",CBC,"\0\0\0\0\0\0\0\0",pad = None, padmode = PAD_PKCS5)
        print("Image Bin", img)
        enc = key.encrypt(img)
        enc1 = key.encrypt(enc)
        enc2 = key.encrypt(enc1)
        fin.close()
        fin = open(Image,'wb')
        fin.write(enc2)
        fin.close()
        print('Image has been encrypted successfully')

    except Exception :
        print(Exception.__name__)
        
    return enc2

def TDES_decrypt(Image):
    try:
     fin = open(Image,'rb')
     image = fin.read()
     fin.close()
     key = des("DESCRYPT",CBC,"\0\0\0\0\0\0\0\0",pad = None, padmode = PAD_PKCS5)
     dec = key.decrypt(image)
     dec1 = key.decrypt(dec)
     dec2 = key.decrypt(dec1)
     fin = open(Image,'wb')
     fin.write(dec2)
     fin.close()
    except Exception:
        print(Exception.__name__)

    return dec2

  
path = r'C:\Users\Admin\Pictures\Sample Image 4.jfif'
ed2 = TDES_encrypt(path)
print("Final Encryption : %r" %ed2)
d2 = TDES_decrypt(path)
print("Final decryption : %r" %d2)







