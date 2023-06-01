# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original
# array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
# be [2, 3, 6].
from typing import List


def get_all_except_index(array: List[int], index: int) -> List[int]:
    new_array = []
    for i, v in enumerate(array):
        if i != index:
            new_array.append(v)

    return new_array


def get_product_of_array(array: List[int]) -> int:
    product = 1
    for element in array:
        product *= element

    return product


def create_array_from_products(array: List[int]) -> List[int]:
    new_array = []
    for i, v in enumerate(array):
        temp_array = get_all_except_index(array, i)
        product = get_product_of_array(temp_array)
        new_array.append(product)

    return new_array


list_ = [1, 2, 3, 4, 5]
print(create_array_from_products(list_))
