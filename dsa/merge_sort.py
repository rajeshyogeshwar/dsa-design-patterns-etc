"""Merge Sort.

Algorithm:
1: If length of array is greater than 1, partition the array at mid.
2: Recursively call sort over the two halves created by step 1.
"""
from typing import List


def sort(array: List[int]) -> List[int]:
    """Implementation of selection sort algorithm."""

    if len(array) > 1:

        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        sort(array=left)
        sort(array=right)

        left_itr = 0
        right_itr = 0
        array_itr = 0

        while left_itr < len(left) and right_itr < len(right):

            if left[left_itr] <= right[right_itr]:
                array[array_itr] = left[left_itr]
                left_itr += 1
                array_itr += 1
            else:
                array[array_itr] = right[right_itr]
                right_itr += 1
                array_itr += 1

        if left_itr < len(left):
            while left_itr < len(left):
                array[array_itr] = left[left_itr]
                left_itr += 1
                array_itr += 1

        elif right_itr < len(right):
            while right_itr < len(right):
                array[array_itr] = right[right_itr]
                right_itr += 1
                array_itr += 1

    return array


if __name__ == "__main__":

    array = [
        782,
        355,
        928,
        130,
        68,
        658,
        243,
        846,
        77,
        793,
        46,
        20,
        947,
        802,
        591,
        701,
        372,
        529,
        695,
        213,
    ]
    sorted_array = sort(array=array)
    print(sorted_array)
