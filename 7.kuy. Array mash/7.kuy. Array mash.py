def array_mash(a, b):
    return [x for y in zip(a, b) for x in y]
