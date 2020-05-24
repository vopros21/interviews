# Given an array of integers, and an integer ‘K’, find the count of pairs
# of elements in the array whose sum is equal to 'K'.
#
# Input:
# First line of the input contains an integer T, denoting the number
# of test cases. Then T test cases follow. Each test case consists of
# two lines. First line of each test case contains 2 space separated
# integers N and K denoting the size of array and the sum respectively.
# Second line of each test case contains N space separated integers
# denoting the elements of the array.
#
# Output:
# Print the count of pairs of elements in the array whose sum is equal to the K.
#
# Constraints:
# 1<=T<=50
# 1<=N<=50
# 1<=K<=50
# 1<=A[i]<=100
#
# Example:
# Input
# 2
# 4 6
# 1 5 7 1
# 4 2
# 1 1 1 1
# Output
# 2
# 6


number = int(input('Input number of cases: '))
while number > 0:
    number -= 1
    count = 0
    size_of_array, summa = list(map(int, input('Input size of array and sum: ').split()))
    array = list(map(int, input('Input elements of array: ').split()))
    for i, elem in enumerate(array):
        for j in range(i + 1, len(array)):
            if elem + array[j] == summa:
                count += 1
    print(f'Number of pairs is {count}')
