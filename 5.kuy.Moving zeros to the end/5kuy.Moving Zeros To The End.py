'''
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]'''


# Using buble sorting
def move_zeros(lst=[1, 2, 0, 1, 0, 1, 0, 3, 0, 1]):
    count = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[count], lst[i] = lst[i], lst[count]
            count += 1
    return lst


# using list methods

def move_zeros(lst=[1, 2, 0, 1, 0, 1, 0, 3, 0, 1]):
    for x in lst:
        if x == 0:
            lst.remove(x)
            lst.append(x)
    return lst
