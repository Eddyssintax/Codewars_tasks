def bubblesort_once(arr=[9, 7, 5, 3, 1, 2, 4, 6, 8]):
    lst = arr[:]
    n = len(lst)
    for j in range(n - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst

print(bubblesort_once())