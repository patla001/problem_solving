#!/bin/python

# Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. 
# The function returns the modified list.

def remove_duplicates(nums):
    # navite algorithm
    # traverse the list
    # if statement to check if the current element is equal to the next element
    # remove the element

    # optimal algorithm
    # convert into a set


    return list(set(nums))

# Example Input: nums = [1,1,1,2,3,4,4,5,6,6]
# Example Output: no_dups = [1,2,3,4,5,6]

if '__main__' == __name__:
    nums = [1,1,1,2,3,4,4,5,6,6]
    print(f'Input: {nums}')
    no_dups = remove_duplicates(nums)
    print(f'Output: {no_dups}')