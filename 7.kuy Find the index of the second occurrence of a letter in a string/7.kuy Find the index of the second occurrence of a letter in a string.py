def second_symbol(s, symbol):
    return s.find(symbol, s.find(symbol)+1)   

print(second_symbol('Hello world!!!','l'))