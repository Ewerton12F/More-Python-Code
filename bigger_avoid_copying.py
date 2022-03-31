def bigger_rec(l,lengh):
    if lengh == 1:
        return l[0]
    last = l[lengh-1]
    sub_l = bigger_rec(l,lengh-1)
    if last > sub_l:
        bigger = last
    else:
        bigger = sub_l
    return bigger

def bigger(l):
    return bigger_rec(l, len(l))

l = [1,12,0,1,2,3,4,10,5,6,7,8,9,11,10]

print(bigger(l))