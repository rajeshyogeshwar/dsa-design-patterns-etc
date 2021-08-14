"""Max heapify """
from typing import List


def heapify(array: List[int], position: int):
    """Max heapify implementation."""
    length = len(array)

    # Assuming that the element at position is largest
    idx_of_largest_element = position
    left_child_idx = 2 * position + 1
    right_child_idx = 2 * position + 2

    if (
        left_child_idx < length
        and array[left_child_idx] > array[idx_of_largest_element]
    ):
        idx_of_largest_element = left_child_idx

    if (
        right_child_idx < length
        and array[right_child_idx] > array[idx_of_largest_element]
    ):
        idx_of_largest_element = right_child_idx

    # If based upon previous comparisons, value of position changes
    if idx_of_largest_element != position:
        array[position], array[idx_of_largest_element] = (
            array[idx_of_largest_element],
            array[position],
        )

        heapify(array=array, position=idx_of_largest_element)


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