"""Heap Sort."""

from typing import List


def max_heapify(array: List[int], length: int, position: int):
    """Max heap implementation."""

    idx_of_largest_element = position
    left_idx = 2 * position + 1
    right_idx = 2 * position + 2

    if left_idx < length and array[left_idx] > array[idx_of_largest_element]:
        idx_of_largest_element = left_idx

    if right_idx < length and array[right_idx] > array[idx_of_largest_element]:
        idx_of_largest_element = right_idx

    if idx_of_largest_element != position:
        array[position], array[idx_of_largest_element] = (
            array[idx_of_largest_element],
            array[position],
        )
        max_heapify(array=array, length=length, position=idx_of_largest_element)


def sort(array: List[int]) -> List[int]:
    """Heap sort."""

    last_non_leaf_node_position = len(array) // 2 - 1

    for idx in range(last_non_leaf_node_position, -1, -1):
        max_heapify(array=array, length=len(array), position=idx)

    # Traverse through all the nodes in reverse order and swap the current element with root element and call max_heapify
    for idx in range(len(array) - 1, 0, -1):
        array[idx], array[0] = array[0], array[idx]
        max_heapify(array=array, length=idx, position=0)

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
        333,
    ]

    sorted_array = sort(array=array)
    print(sorted_array)
