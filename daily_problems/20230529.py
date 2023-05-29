# Problem #1
# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is
# 17.
from typing import List


def is_sum_of_elements(list_: List[int], k: int) -> bool:
    for i, number in enumerate(list_):
        numbers_to_check = list_[i+1:]
        for n in numbers_to_check:
            is_sum = number + n == k
            if is_sum:
                return True

    return False


list_ = [2, 8, 19, 23, 65, 14, 34, 12, 26]
k = 32

print(is_sum_of_elements(list_, k))
