message = input("Enter the Caeser encrypted message: ")

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = symbol_index - key
            if translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)
            translated = translated + SYMBOLS[translated_index]
        else:
            translated = translated + symbol
    print('Key #%s: %s' % (key, translated))
