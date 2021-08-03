def fib_number(n: int):
    array = [0, 1] + [0] * (n - 1)
    for i in range(2, n+1):
        array[i] = array[i-1] + array[i-2]
    return array[n]
