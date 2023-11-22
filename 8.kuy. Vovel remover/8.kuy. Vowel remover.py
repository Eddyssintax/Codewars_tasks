'''Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
don't worry about uppercase vowels
y is not considered a vowel for this kata'''

#using replace method
def shortcuts(s):
    for x in "aeiou":
        s = s.replace(x, "")
    return s

#using list comprehension  

def shortcut( s ):
    return "".join(x for x in s if x not in "aeiou")
