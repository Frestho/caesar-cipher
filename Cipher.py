import random
#sets the caesar cipher key
key = random.randint (1, 25)
#gives you the key, remove this for it to be secret.
print (key)
letters = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
phrase = input('Type a phrase to be encoded: ')
#defines the variable that will store the encoded phrase
encoded = ''
#loop that goes through every character in the inputted phrase and changes the letters according to the key
for place in range(0, len(phrase)):
    inCaps = caps.find(phrase[place])
    if inCaps < 26 and inCaps > -1: #should only be true if there was a capital letter
            phrase2 = ''#this variable handles some temporary stuff
            for i in range (0, len(phrase)): #goes through the user input, ready to replace the capital letter with a lowercase
                if i == place: #am I at the capital letter? if so add it to code 2 from the lowercase letter list
                    phrase2 += letters[inCaps]
                else: #otherwise, do nothing different
                    phrase2 += phrase[i]
            phrase = phrase2 
    placeInLetters = letters.find(phrase[place]) #finds the place that the letter is on in the letters variable
    if not(placeInLetters < 25 and placeInLetters > -1):#if not a letter, don't do anything
        encoded = encoded + phrase[place]
    else: #and if it's a letter, encode it.
        encoded = encoded + letters[(placeInLetters+key) % 26]
print (encoded)
