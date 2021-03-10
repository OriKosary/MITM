# f = open(r'C:\Users\oriko\Desktop\test.txt', 'wb')
# f.write(bytes(('ori'), ('kosary')))
# f.close()

# a = pubkey.save_pkcs1(format='DER')
# b = rsa.key.PublicKey.load_pkcs1(a, format='DER')


from encrypter import *


e = Encrypter()

print(e.encrypt(bytes("hi"),))
#
# dic = {'1': 1, '2': 2, '3': 3}
# a = dic.items()
# vals = []
# keys = []
# for tup in a:
#     keys.append(tup[1])
#     vals.append(tup[0])
# print(vals)
# print(keys)
#
# dickoru = {}
# for i in keys:
#     dickoru[keys[i]] = vals[i]
#
# print(dickoru)
#
#

# class Human:
#     def __init__(self, height, name, eye_color, girlfriend):
#         self.height = height
#         self.name = name
#         self.eye_color = eye_color
#         self.girlfriend = None
#
#     def is_fat(self):
#         if self.height > 180:
#             print(self.name + " YOU A FATTY")
#
#
# a = Human(187, 'NIGERO', 'blue', None)
# a.is_fat()
#
#
#
#
# def is_slice(lst, num):
#     length = len(lst)
#     sum = 0
#     for i in lst:
#         if i % length//3 == 0:
#             if sum >= num:
#                 return False
#             else:
#                 sum = 0
#     return True



