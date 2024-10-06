#!/bin/python

# Problem 1: Remove Vowels

# Write a function remove_vowels() that takes in a string s as a parameter and returns 
# a new string with all the vowels removed. For the purposes of this exercise, 
# consider a, e, i, o, and u as vowels and not y. The function should preserve the case of the original letters.

def remove_vowels(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, "")
    return s

# Example Usage:

# s = "Hello World"
# new_string = remove_vowels(s)
# print(new_string)

# Example Output: Hll Wrld

if __name__ == "__main__":
    s = "Hello World"
    print(f"Input: {s}")
    print(f"Output: {remove_vowels(s)}")
    
    s = "Python Programming"
    print(f"Input: {s}")
    print(f"Output: {remove_vowels(s)}")
    
    s = "I love Python"
    print(f"Input: {s}")
    print(f"Output: {remove_vowels(s)}")
    
    