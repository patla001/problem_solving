#!/bin/python

# Problem 1: Sum of Strings

# Write a function sum_of_number_strings() that takes in a list of strings nums. 
# Each string is a representations of integers. The function should return the sum of these strings as an integer.

def sum_of_number_strings(nums):
    # traverse the num list
    summation = 0
    for i in nums:
        #print(int(i))
    # summation of each element
        summation = summation + int(i)
    #print(summation)
    # return the summation of the list
    return summation

# Example Usage:
if '__main__' == __name__:
    nums = ["10", "20", "30"]
    print(f'Input: {nums}')
    sum = sum_of_number_strings(nums)
    print(f'Output: {sum}')
# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)

# Example Output: 60