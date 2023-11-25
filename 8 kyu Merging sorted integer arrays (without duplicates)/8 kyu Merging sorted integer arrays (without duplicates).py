'''Write a function that merges two sorted arrays into a single one. The arrays only contain integers. 
Also, the final outcome must be sorted and not have any duplicate.

'''
#using set for deleting dublicates
def merge_arrays(first, second):
    return sorted(list(set(first + second)))


#using dict method for faster solution

def merge_arrays(first, second):
    return sorted(dict.fromkeys(first + second).keys())