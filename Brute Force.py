letters = 'abcdefghijklmnopqrstuvwxyz'
code = input('Put your encoded Caesar Cipher here: ')
for key in range (0, 25):
    holder = ''
    for place in range (0, len(code)):
        placeInLetters = letters.find(code[place])
        if not(placeInLetters < 25 and placeInLetters > -1):
            holder = holder + code[place]
        else:
            holder = holder + letters[(placeInLetters+key) % 26]
    print (holder)
