"""Insertion Sort.

Algorithm:
1: Iterate over the length of the array.
2: Compare the current element to its predecessor.
3: If the current element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

Time Complexity: O(n^2)
"""

from typing import List


def sort(array: List[int]) -> List[int]:
    """Implementation of insertion sorting algorithm."""

    for idx in range(len(array)):

        temp = array[idx]
        i_idx = idx - 1

        while i_idx > -1 and array[i_idx] > temp:
            array[i_idx + 1] = array[i_idx]
            i_idx -= 1

        array[i_idx + 1] = temp

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
