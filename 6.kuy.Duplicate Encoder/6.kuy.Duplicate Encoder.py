# using list comprehation
def duplicate_encode(word):
    return "".join("(" if word.lower().count(x) == 1 else ")" for x in word.lower())

# using saving in variable


def duplicate_encode(word):
    var = ""
    for x in word.lower():
        if word.lower().count(x) == 1:
            var += "("
        else:
            var += ")"
    return var
