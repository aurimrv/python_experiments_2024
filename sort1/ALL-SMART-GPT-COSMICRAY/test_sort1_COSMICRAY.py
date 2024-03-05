import pytest
from sort1 import Sort 

# Test cases for Selection Sort
def test_selection_sort0():
    assert Sort.selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert Sort.selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert Sort.selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Test cases for Insertion Sort
def test_insertion_sort():
    assert Sort.insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert Sort.insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert Sort.insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Test cases for Merge Sort
def test_merge_sort():
    assert Sort.merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert Sort.merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert Sort.merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Test cases for Quick Sort
def test_quick_sort():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    arr = [5, 4, 3, 2, 1]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1, 2, 3, 4, 5]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

def test_partition_elements_right_of_pivot():
    # Test an array with multiple elements
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    # Perform the partition
    result_pivot = Sort.partition(arr.copy(), 0, len(arr) - 1)

    # Elements to the right of the pivot should be greater than the pivot
    assert all(element > arr[result_pivot] for element in arr[result_pivot + 1:])
