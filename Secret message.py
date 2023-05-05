alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'xznlwebgjhqdyvtkfuompciasr'
secret_message = input('Enter your message: ')
secret_message = secret_message.lower()
for n in secret_message:
    if n.isalpha():
        print(key[alphabet.index(n)], end='')
    else:
        print(n, end='')


