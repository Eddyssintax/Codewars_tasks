'''Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.'''
#using hash table

def get_count(sentence):
    dct = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for word in sentence:
        for letter in word:
            if letter.lower() in dct:
                dct[letter] += 1
        
    nums = 0
    for count in dct.values():
            nums += count
    return nums

#using sum inside of loop
def get_count(sentence):
    return sum(1 for x in sentence if x in "aeiou")