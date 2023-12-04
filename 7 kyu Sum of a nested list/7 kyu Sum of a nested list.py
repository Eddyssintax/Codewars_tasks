'''Implement a function to calculate the sum of the numerical values in a nested list. 
For example :

sum_nested([1, [2, [3, [4]]]]) -> 10'''

def sum_nested(lst):
    total = 0

    for num in lst:
        if type(num) == list:
            total += sum_nested(num)
        else:
            total += num
    return total