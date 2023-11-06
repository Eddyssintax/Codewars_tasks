def sum_even_numbers(i):
    return sum(x for x in i if x % 2 == 0)

print(sum_even_numbers([1, 2, 35, 7, 8, 9, 10]))