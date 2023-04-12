# https://leetcode.com/problems/boats-to-save-people/
from pprint import pprint
# Runtime: ms: beats %
# Memory: MB: beats %
from typing import List


def num_rescue_boats(self, people: List[int], limit: int) -> int:
    count = [0] * (limit + 1)
    for weight in people:
        count[weight] += 1
    pprint(count)


if __name__ == "__main__":
    p = [3,5,3,4]
    lim = 5
    print(num_rescue_boats(self=None, people=p, limit=lim))
