"""Quick Sort.

Algorithm:
1: Pick a pivot [In our case, the first element]
2: Place the pivot element in it's correct place. Now, the items to left of pivot are smaller and on it's right are greater.
3: 1 & 2 form what is called partitioning method and it needs to be called recursively on the left and right partitions.

Time Complexity: 0(n^2)

"""
from typing import List


def partition(array: List[int], low: int, high: int) -> int:
    """Partition method."""

    pivot = array[low]
    start = low
    end = high

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1
        while end > -1 and array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    array[low], array[end] = array[end], array[low]
    return end


def sort(array: List[int], low: int, high: int) -> List[int]:
    """Implementation of quick sort algorithm."""
    if low < high:
        p_idx = partition(array=array, low=low, high=high)
        sort(array=array, low=low, high=p_idx)
        sort(array=array, low=p_idx + 1, high=high)

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
    sorted_array = sort(array=array, low=0, high=len(array) - 1)
    print(sorted_array)
