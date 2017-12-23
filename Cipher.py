import random
#sets the caesar cipher key
key = random.randint (1, 25)
#gives you the key, remove this for it to be secret.
print (key)
letters = 'abcdefghijklmnopqrstuvwxyz'
phrase = input('Type a phrase to be encoded: ')
#defines the variable that will store the encoded phrase
encoded = ''
#main function that encrypts your phrase under the key. only letters are affected
def encode():
    global encoded
    for place in range(0, len(phrase)):
        #finds the place that the letter is on in the letters variable
        placeInLetters = letters.find(phrase[place])
        #if not a letter, don't do anything
        if not(placeInLetters < 25 and placeInLetters > -1):
            encoded = encoded + phrase[place]
        #and if it's a letter, encode it.
        else:
            encoded = encoded + letters[(placeInLetters+key) % 26]
encode()
print (encoded)    
