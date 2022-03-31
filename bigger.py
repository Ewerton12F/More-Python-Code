def bigger_rec(l):
    lengh = len(l)
    if lengh == 1:
        return l[0]
    last = l[-1]
    sub_l = bigger_rec(l[:-1])
    if last > sub_l:
        bigger = last
    else:
        bigger = sub_l
    return bigger

l = [1,0,1,2,3,4,10,5,6,7,8,9,11,10]

print(bigger_rec(l))