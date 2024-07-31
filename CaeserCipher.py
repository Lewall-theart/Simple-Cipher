#Caesar cipher

import pyperclip

message = input("Enter the message: ")

key = int(input("Enter the key: "))

mode = 'encrypt'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy1234567890 !?.'

translated = ''

for symbol in message:
  if symbol in SYMBOLS:
    symbolIndex = SYMBOLS.find(symbol)

    if mode == 'encrypt':
        translatedIndex = symbolIndex + key
    elif mode == 'decrypt':
        translatedIndex = symbolIndex - key

    if translatedIndex >= len(SYMBOLS):
        translatedIndex = translatedIndex - len(SYMBOLS)
    elif translatedIndex < 0:
        translatedIndex = translatedIndex + len(SYMBOLS)

    translated = translated + SYMBOLS[translatedIndex]
  else:
    translated = translated + symbol

print(translated)
pyperclip.copy(translated)

