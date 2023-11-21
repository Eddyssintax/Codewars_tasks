def duplicate_count(text):
    num = {}
    for dub in text.lower():
        num[dub] = num.get(dub, 0) + 1
    count = 0
    
    for  v in num.values():
        if v > 1:
            count += 1
    return count