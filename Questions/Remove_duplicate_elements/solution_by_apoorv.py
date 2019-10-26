def removeduplicates(li):
    li = list(dict.fromkeys(li))
    return li


li = [1, 9, 2, 3, 5, 5, 3, 4, 2, 1, 9]
print(removeduplicates(li))
