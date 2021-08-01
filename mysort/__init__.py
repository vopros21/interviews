import random
import mysort.merge_sort


if __name__ == '__main__':
    new_list = random.sample(range(10), 10)
    print(*new_list)
    mysort.merge_sort.merge_sort(new_list)
    print(*new_list)
