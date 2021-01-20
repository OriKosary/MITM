# f = open(r'C:\Users\oriko\Desktop\test.txt', 'wb')
# f.write(bytes(('ori'), ('kosary')))
# f.close()

# a = pubkey.save_pkcs1(format='DER')
# b = rsa.key.PublicKey.load_pkcs1(a, format='DER')


from encrypter import *


e = Encrypter()
a = e.rsa_public_key.save_pkcs1(format='DER')
print(a)