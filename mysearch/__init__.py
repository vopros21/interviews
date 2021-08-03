import random

import mysearch.binary_search
import mysort

if __name__ == '__main__':
    array = random.sample(range(10), 5)
    print(f'Unsorted array: {array}')
    element = array[0]
    mysort.quick_sort_hoare.hoare_sort(array)
    print(f'Sorted array: {array}')
    print('Position of existed element: ', mysearch.binary_search.search(array, element))
    print('Position of not existed element: ', mysearch.binary_search.search(array, element + 15))
