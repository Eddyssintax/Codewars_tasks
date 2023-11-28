'''utput
Output will consist of a list of string values (in Haskell and C: Open or Senior) 
stating whether the respective member is to be placed in the senior or open category.

Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
'''

def open_or_senior(data):
    return ["Senior" if x[0] > 54 and x[1] > 7 else "Open" for x in data]