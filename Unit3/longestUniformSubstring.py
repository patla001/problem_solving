#!/bin/python

# Problem 4: Longest Uniform Substring

# Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. 
# A uniform substring consists of a single repeated character.

def longest_uniform_substring(s):
    
    count_dict = {}
    for i in s:
        count_dict[i] = s.count(i)
    
    return max(count_dict.values())

# Example Usage:

# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s2 = "abcdef"
# l2 = longest_uniform_substring(s2)
# print(l2)

# Example Output:

# 4
# 1

if __name__ == '__main__':
    s1 = "aabbbbCdAA"
    l1 = longest_uniform_substring(s1)
    print(f"Input: {s1}")
    print(f"Output: Longest uniform substring count {l1}")

    s2 = "abcdef"
    l2 = longest_uniform_substring(s2)
    print(f"Input: {s2}")
    print(f"Output: Longest uniform substring count {l2}")