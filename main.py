text_input = str(input("Please enter text to be crypted:")).lower()

alphabet_positions = {}
for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    alphabet_positions[letter] = index + 1

def Crypt_abc(text):
        final_text = ""
        for character in text:
            if character.isalpha():
                final_text = final_text + str(alphabet_positions[character])
            elif character == ' ':
                final_text = final_text + "x"
            else:
                final_text = final_text + character
            final_text = final_text + "w"
        return final_text

print(Crypt_abc(text_input))

with open("crypted_text.txt", "w") as file:
    file.write(Crypt_abc(text_input))

input()

