from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


class Encrypter:
    def __init__(self):
        key = RSA.generate(1024)
        self.private_key = key.export_key('PEM')
        self.public_key = key.publickey().exportKey('PEM')

        # rsa_public_key = RSA.importKey(public_key)
        # rsa_public_key = PKCS1_OAEP.new(rsa_public_key)

        # rsa_private_key = RSA.importKey(private_key)
        # rsa_private_key = PKCS1_OAEP.new(rsa_private_key)



    # def encrypt(self, string):
    #     string_b = str.encode(string)
    #     encrypted_text = self.rsa_public_key.encrypt(string_b)
    #     return encrypted_text
    #
    # def decrypt(self, string):  # type -> Bytes
    #     decrypted_text = self.rsa_private_key.decrypt(string)
    #     return decrypted_text


# def rsa_encrypt_decrypt():
#     key = RSA.generate(1024)
#     private_key = key.export_key('PEM')
#     public_key = key.publickey().exportKey('PEM')
#     message = input('plain text for RSA encryption and decryption:')
#     message = str.encode(message)
#
#     rsa_public_key = RSA.importKey(public_key)
#     rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
#     encrypted_text = rsa_public_key.encrypt(message)
#
#     print('your encrypted_text is : {}'.format(encrypted_text))
#
#     rsa_private_key = RSA.importKey(private_key)
#     rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
#     decrypted_text = rsa_private_key.decrypt(encrypted_text)
#
#     print('your decrypted_text is : {}'.format(decrypted_text))
#
#

e = Encrypter()

