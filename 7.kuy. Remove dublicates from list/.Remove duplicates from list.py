# using enumerate
def distinct(seq):
    return [val for idx, val in enumerate(seq) if val not in seq[:idx]]

# using dict fromkeys


def distinct(seq):
    return list(dict.fromkeys(seq))
