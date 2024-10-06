#!/bin/python

# Problem 6: Interleave Lists

# Write a function interleave_lists() that accepts two lists as parameters. 
# The function should return a new list that combines the given lists 
# by alternating which list it takes its next element from. 
# It will take elements in order, and if one list is longer 
# it will append the remaining elements to the end of the interleaved list.

def interleave_lists(lst1, lst2):
    inter_lst = []
    nlst1 = len(lst1)
    nlst2 = len(lst2)
    max_len = max(len(lst1), len(lst2))
    for i in range(max_len):
        if i < nlst1:
            inter_lst.append(lst1[i])
        if i < nlst2:
            inter_lst.append(lst2[i])
    return inter_lst

# Example Usage:

# lst1 = [1, 2, 3, 4]
# lst2 = [10, 20]
# inter_lst = interleave_lists(lst1, lst2)
# print(inter_lst)

# Example Output:

# [1, 10, 2, 20, 3, 4]

if __name__ == "__main__":
    lst1 = [1, 2, 3, 4]
    lst2 = [10, 20]
    print(f"Input: {lst1}, {lst2}")
    print(f"Output: {interleave_lists(lst1, lst2)}")
    
    lst3 = [1, 2, 3]
    lst4 = [10, 20, 30, 40]
    print(f"Input: {lst3}, {lst4}")
    print(f"Output: {interleave_lists(lst3, lst4)}")