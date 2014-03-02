def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    if (char == 'a' or char == 'e' or char =='i' or char == 'o' or char == 'u'):
        return True
    elif (char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        return True
    else:
        return False

def vowelcheck(s):
    '''
    s: a string containing a word
    returns: the number of vowels in s
    '''
    count = 0
    for i in range(len(s)):
        if (isVowel(s[i])):
            count = count + 1
    return count

print "Number of vowels: " +str(vowelcheck(s))