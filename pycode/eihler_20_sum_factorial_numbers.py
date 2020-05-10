def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def sum_of_numbers(number):
    return number % 10 + sum_of_numbers(number // 10) if len(str(number)) > 1 else number


n = 10
k = factorial(n)
print(f'Factorial {n} equals {k}')
print(f'Sum of factorial numbers equals {sum_of_numbers(k)}')
