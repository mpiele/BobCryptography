#generate dictionaries with letters and their position in the alphabet
alphabet_positions = {}
for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    alphabet_positions[letter] = index + 1

#reverse the aplhabet_positions dictionary
alphabet_positions_reversed = {value: key for key, value in alphabet_positions.items()}

#function used to encrypt text using the ABC cryptography algorithm
def Encrypt_ABC(text):
        final_text = ""
        for character in text.lower():
            if character.isalpha():
                final_text = final_text + str(alphabet_positions[character])
            elif character == " ":
                final_text = final_text + "x"
            else:
                final_text = final_text + character
            final_text = final_text + "w"
        return final_text

#function used to decrypt text using the ABC cryptography algorithm
def Decrypt_ABC(text):
        final_text = ""
        def separate_string(string):
            characters = string.split("w")
            return characters
        for character in separate_string(text):
            if character.isdigit():
                final_text = final_text + str(alphabet_positions_reversed[int(character)])
            elif character == "x":
                final_text = final_text + " "
            else:
                final_text = final_text + character
        return final_text
