limit = 1000
a = 2
b = 3
c = 995

while c > a + b:
    if c * c == a * a + b * b:
        break
    c -= 1
    b += 1
    m = a
    n = b
    while m < n:
        m += 1
        n -= 1
        if c * c == m * m + n * n:
            a = m
            b = n
            break
print(f'{a} + {b} + {c} = 1000')
