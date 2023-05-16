# BobCryptography

A python library that can encrypt and decrypt strings with ease.

## Installation

Download the ```bobcrypt.py``` file and put it in the same folder as your project files.
Make sure to import it at the top of your program:

```python
from bobcrypt import Encrypt_ABC, Decrypt_ABC 
```

## Usage
Currently consists of only two functions, ```Encrypt_ABC()``` and ```Decrypt_ABC()```, which use the ABC encrypting algorithm, developed by our team.

```python
#import the encrypt and decrypt functions
from bobcrypt import Encrypt_ABC, Decrypt_ABC

#encrypts the string "hello, world!", should output "8w5w12w12w15w,wxw23w15w18w12w4w!w"
print(Encrypt_ABC("hello, world!"))

#decrypts the string "8w5w12w12w15w,wxw23w15w18w12w4w!w", should output "hello, world!"
print(Decrypt_ABC("8w5w12w12w15w,wxw23w15w18w12w4w!w"))
```

## How it works
The ABC encrypting algorithm converts every letter to its corresponding position in the alphabet, 
transforms every blank space ```" "``` into an ```"x"```,
adds a ```"w"``` after each converted character, 
and every other character stays the same.

## Contributing

Pull requests are welcome.
