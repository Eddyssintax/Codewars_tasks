# easy method. time: ~570ms
def merge_arrays(a, b):
    return sorted(set(a + b))


# using dict. time ~510ms
def merge_arrays(first, second):
    return sorted(dict.fromkeys(first + second).keys())
