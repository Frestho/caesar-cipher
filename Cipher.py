import random
#sets the caesar cipher key
key = random.randint (1, 25)
print (key)
letters = 'abcdefghijklmnopqrstuvwxyz'
phrase = input('Type a phrase to be encoded: ')
encoded = ''
def encode():
    global encoded
    for place in range(0, len(phrase)):
        placeInLetters = letters.find(phrase[place])
        if not(placeInLetters < 25 and placeInLetters > -1):
            encoded = encoded + phrase[place]
        else:
            encoded = encoded + letters[(placeInLetters+key) % 26]
encode()
print (encoded)    
