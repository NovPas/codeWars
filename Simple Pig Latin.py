# Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    return ' '.join(s[1:]+s[0]+'ay' if s.isalpha() else s for s in text.split())


print(pig_it('O tempora o mores !'))
