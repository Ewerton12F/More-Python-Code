def sum_rec(l):
    if len(l) == 0:
        return 0
    return l[-1] + sum_rec(l[:-1])

l = [1,2,3,4,5,6]
print(f'List elements sum: {sum_rec(l)}')