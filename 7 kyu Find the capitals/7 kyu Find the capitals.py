'''Instructions
Write a function that takes a single string (word) as argument. 
The function must return an ordered list containing the indexes of all capital letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]
'''
def capitals(word):
    lst = []
    
    for i, x in enumerate(word):
        if x.isupper():
            lst.append(i)
    return lst