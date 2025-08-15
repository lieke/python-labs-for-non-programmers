def first_element(lst):
    return lst[0]

def sum_of_list(lst):
    return sum(lst)

def last_element(lst: list):
    return lst[-1]

def sort_list(lst: list):
    return sorted(lst)

def isOdd(num):
    return num % 2 != 0

def find_odd_numbers(lst: list):
    return list(filter(isOdd, lst))

def calculate_sum_of_same_positioned_elements(lst1: list, lst2: list):
    return [x + y for x, y in zip(lst1, lst2)]