'''You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3'''

#using list comprehension + slicing
def stray(arr):
    return [x for x in arr if arr.count(x) == 1][0]


# using hash tables(like always)
def stray(arr):
    dct = {}

    for nums in arr:
        dct[nums] = dct.get(nums, 0)+ 1
    
    un_num = 0
    for key, value in dct.items():
        if value == 1 :
            un_num += key
    return un_num

