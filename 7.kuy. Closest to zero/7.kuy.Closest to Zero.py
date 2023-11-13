def closest(lst):
    return sorted((lst), key=abs)[0]


print(closest([2, 4, -1, -3]))
