def search_rec(l, n):
    lengh = len(l)
    if lengh == 0:
        return False
    if l[-1] == n:
        return lengh-1
    return search_rec(l[:-1], n)

l = [0,1,2,3,4,5,6,7,8,9]
n = int(input())

print(search_rec(l, n))