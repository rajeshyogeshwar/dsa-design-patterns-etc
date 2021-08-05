"""Min Heap."""

from typing import List


def heapify(array: List[int], position: int):
    """Min heap implementation."""

    idx_of_smallest_element = position
    left_idx = 2 * position + 1
    right_idx = 2 * position + 2

    if left_idx < len(array) and array[left_idx] < array[idx_of_smallest_element]:
        idx_of_smallest_element = left_idx

    if right_idx < len(array) and array[right_idx] < array[idx_of_smallest_element]:
        idx_of_smallest_element = right_idx

    if idx_of_smallest_element != position:
        array[position], array[idx_of_smallest_element] = (
            array[idx_of_smallest_element],
            array[position],
        )
        heapify(array=array, position=idx_of_smallest_element)


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

    # build_heap(array=array)
    last_non_leaf_node_position = (len(array) // 2) - 1

    # Traversing in reverse order all the non-leaf nodes
    for idx in range(last_non_leaf_node_position, -1, -1):
        heapify(array=array, position=idx)

    print(array)