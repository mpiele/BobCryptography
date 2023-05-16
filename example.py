#EXAMPLE OF USE

#import the encrypt and decrypt functions
from bobcrypt import Encrypt_ABC, Decrypt_ABC

#encrypts the string "hello, world!", should output "8w5w12w12w15w,wxw23w15w18w12w4w!w"
print(Encrypt_ABC("hello, world!"))

#decrypts the string "8w5w12w12w15w,wxw23w15w18w12w4w!w", should output "hello, world!"
print(Decrypt_ABC("8w5w12w12w15w,wxw23w15w18w12w4w!w"))
