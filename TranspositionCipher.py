#simple transposition cipher

def encrypt(message, key):
    encrypted_message = [''] * key
    for col in range(key):
        position = col
        for row in range(len(message)//key +1):
            if position < len(message):
                encrypted_message[col] += message[position]
            position += key
    return ''.join(encrypted_message)

def decrypt(encrypted_message, key):
    num_of_columns = len(encrypted_message) // key
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(encrypted_message)
    plaintext = [''] * num_of_columns
    col = 0
    row = 0
    for symbol in encrypted_message:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

message = input("Enter the message: ")
key = int(input("Enter the key: "))

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
