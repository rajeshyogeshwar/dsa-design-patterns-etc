"""Selection Sort.

Algorithm:
1: Iterate over the length of array.
2: Mark the current item as min.
3: Iterate over the subarray [min to length of array].
4: If the element is smaller than min, then swap.

Time Complexity: O(n^2)
"""
from typing import List


def sort(array: List[int]) -> List[int]:
    """Implementation of selection sort algorithm."""

    for idx in range(len(array)):
        min = idx
        for i_idx in range(idx, len(array)):
            if array[i_idx] < array[min]:
                min = i_idx

        array[idx], array[min] = array[min], array[idx]

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