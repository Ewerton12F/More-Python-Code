def  divisors_rec(n, d):
    if d == 1:
        return [1]
    div_list = divisors_rec(n, d-1)
    if n % d == 0:
        div_list.append(d)
    return div_list

def divisors(n):
    return divisors_rec(n, n)

n = int(input())
print(f'Divisores de {n}: {divisors(n)}')