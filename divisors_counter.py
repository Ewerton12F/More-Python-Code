def div_c_rec(n, d):
    if d == 1:
        return 1
    qtd = div_c_rec(n, d-1)
    if n % d == 0:
        qtd = qtd + 1
    return qtd

def div_c(n):
    return div_c_rec(n, n)

n = int(input())
print(f'O número {n} tem {div_c(n)} divisores.')