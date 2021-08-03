import random

import mysort.quick_sort_hoare
import mysort.merge_sort
import mysort.checking


if __name__ == '__main__':
    new_list = random.sample(range(1000000), 10) + random.sample(range(10), 10)
    print(new_list)
    mysort.quick_sort_hoare.hoare_sort(new_list)
    print(new_list)
    print(mysort.checking.is_sorted(new_list))
