from labs.lists import first_element
from labs.lists import sum_of_list
from labs.lists import last_element
from labs.lists import sort_list
from labs.lists import isOdd
from labs.lists import find_odd_numbers
from labs.lists import calculate_sum_of_same_positioned_elements

def test_first_element():
    assert first_element([1, 2, 3]) == 1
    assert first_element(["a", "b", "c"]) == "a"

def test_sum_of_list():
    assert sum_of_list([1, 2, 3]) == 6
    assert sum_of_list([]) == 0

def test_last_element():
    assert last_element([1, 2, 3]) == 3
    assert last_element(["a", "b", "c"]) == "c"

def test_sort_list():
    assert sort_list([1, 5, 2, 3, 8, 4, 7, 6]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert sort_list(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]
    assert sort_list([]) == []

def test_isOdd():
    assert isOdd(1) == True
    assert isOdd(2) == False
    assert isOdd(3) == True
    assert isOdd(0) == False

def test_find_odd_numbers():
    assert find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert find_odd_numbers([2, 4, 6]) == []
    assert find_odd_numbers([]) == []    

def test_calculate_sum_of_same_positioned_elements():
    assert calculate_sum_of_same_positioned_elements([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert calculate_sum_of_same_positioned_elements([1, 2], [3]) == [4]
    assert calculate_sum_of_same_positioned_elements([], []) == []
    assert calculate_sum_of_same_positioned_elements([1], [2]) == [3]
