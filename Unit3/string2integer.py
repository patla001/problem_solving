#!/bin/python

# Problem 1: String to Integer

# Write a function string_to_integer_mapping() that takes in a string of digits
#  s as a parameter and returns a list where each element 
# is the integer value of the corresponding digit in the string.

def string_to_integer_mapping(s):
    result = []
    for i in s:
        result.append(int(i))
    return result
# Example Input: s="12345"
# Example Output: [1, 2, 3, 4, 5]

if __name__ == "__main__":
    s = "12345"
    print(f"Input: {s}")
    print(f"Output: {string_to_integer_mapping(s)}")
    
    s = "987654321"
    print(f"Input: {s}")
    print(f"Output: {string_to_integer_mapping(s)}")