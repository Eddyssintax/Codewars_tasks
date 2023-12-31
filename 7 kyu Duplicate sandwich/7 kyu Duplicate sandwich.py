'''Task
In this kata you will be given a list consisting of unique elements except for one thing that appears twice.

Your task is to output a list of everything inbetween both occurrences of this element in the list.

Examples:
[0, 1, 2, 3, 4, 5, 6, 1, 7, 8] => [2, 3, 4, 5, 6]
['None', 'Hello', 'Example', 'hello', 'None', 'Extra'] => ['Hello', 'Example', 'hello']
[0, 0] => []
[True, False, True] => [False]
['e', 'x', 'a', 'm', 'p', 'l', 'e'] => ['x', 'a', 'm', 'p', 'l']
Notes
All elements will be the same datatype.
All used elements will be hashable.
'''

def duplicate_sandwich(arr):
    lst = []
    for num, item in enumerate(arr):
        if item not in lst:
            lst.append(item)
        else:
            return arr[arr.index(item)+1 : num]
        