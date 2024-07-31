#Simple substitution ciphered

def encrypt(message, key):
      alphabet = "abcdefghijklmnopqrstuvwxyz"
      encrypted_message = ""

      for char in message:
        char = char.lower()
        if char in alphabet:
          char_index = alphabet.index(char)
          encrypted_char = key[char_index]
          encrypted_message += encrypted_char
        else:
          encrypted_message += char
      return encrypted_message

def decrypt(encrypted_message, key):
      alphabet = "abcdefghijklmnopqrstuvwxyz"
      message = ""
      for char in encrypted_message:
        char = char.lower()
        if char in key:
          char_index = key.index(char)
          decrytped_char = alphabet[char_index]
          message += decrytped_char
        else:
          message += char
      return message


message = input("Enter the message to encrypt: ")
key = "qwertasdfgzxcvbyuijklmnhp"
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
