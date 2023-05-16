#EXAMPLE OF USE

#import the crypt and decrypt functions
from bobcrypt import Crypt_ABC, Decrypt_ABC

#crypts the string "hello, world!", should output "8w5w12w12w15w,wxw23w15w18w12w4w!w"
print(Crypt_ABC("hello, world!"))

#decrypts the string "8w5w12w12w15w,wxw23w15w18w12w4w!w", should output "hello, world!"
print(Decrypt_ABC("8w5w12w12w15w,wxw23w15w18w12w4w!w"))