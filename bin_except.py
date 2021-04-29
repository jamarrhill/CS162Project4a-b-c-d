# Name: Jamar Hill
# Date: 4/25/2021
# Description: CS 162 Project 4a

class TargetNotFound(Exception):
    def __init__(self, message):
        self.message = message

def binary_search(a_list, target):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, returns -1, indicating the target value isn't in the list
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
            middle = (first + last) // 2
            if a_list[middle] == target:
                return middle
            if a_list[middle] > target:
                last = middle - 1
            else:
                first = middle + 1
    raise TargetNotFound(f" {target} was not found in list")


test = [1,2,3,4]
print(binary_search(test,8))
