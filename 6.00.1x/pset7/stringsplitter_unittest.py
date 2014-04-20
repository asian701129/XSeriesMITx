import string
def stringsplitter(self, splitThisString):
    newstring = ''
    for char in splitThisString:
        if char in string.punctuation:
            newstring += ' '
        else:
            newstring += char
    wordsInString = newstring.split(' ')
    return wordsInString

self = 1
print stringsplitter(self, 'eat good food')

print stringsplitter(self, "eat lots'a checki'n")

