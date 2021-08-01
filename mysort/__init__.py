import random

import mysort.quick_sort_hoare
import mysort.merge_sort


if __name__ == '__main__':
    new_list = random.sample(range(15), 10) + random.sample(range(10), 5)
    print(*new_list)
    # mysort.merge_sort.merge_sort(new_list)
    mysort.quick_sort_hoare.hoare_sort(new_list)
    print(*new_list)
