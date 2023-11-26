'''Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.

'''

#using hash table method

def sum_no_dublicates(nums):
    dct = {}

    for num in nums:
        dct[num] = dct.get(num, 0)+1

    uni_num = 0

    for number, count in dct.items():
        if count == 1:
            uni_num += number
    return uni_num

#using list

def sum_no_duplicates(l):
    lst = []
    for num in l:
        if l.count(num) == 1:
            lst.append(num)
    return sum(lst)

#using list comprehension 

def sum_no_duplicates(l):
    return sum([x for x in l if l.count(x) == 1])