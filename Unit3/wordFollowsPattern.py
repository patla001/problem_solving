#!/bin/python

# Problem 3: Word Follows Pattern

# Write a function wordPattern() that takes in a string pattern and a string s as parameters. 
# The function returns True if s follows the pattern and False otherwise. 
# The string follows the pattern if there is a 1:1 correspondence between a letter in the pattern and a non-empty word in s.

def wordPattern(pattern, s):
    words = s.split()
    m = len(pattern)
    n = len(words)
    if m != n:
        return False
    pattern_dict = {}
    word_dict = {}
    for i in range(m):
        if pattern[i] in pattern_dict:
            print(f'pattern_dict[pattern[i]]: {pattern_dict[pattern[i]]} words[i]: {words[i]}')
            if pattern_dict[pattern[i]] != words[i]:
                return False
        else:
            pattern_dict[pattern[i]] = words[i]
        
    return True

# Example Usage:

# pattern = "abba"
# s = "dog cat cat dog"
# print(wordPattern(pattern, s))
# s2 = "dog cat cat fish"
# print(wordPattern(pattern, s2))

# pattern2 = "aaaa"
# s3 = "dog cat dog cat"
# print(wordPattern(pattern2, s3))
# s4 = "dog dog dog dog"
# print(wordPattern(pattern2, s4))

# Example Output:

# True
# False
# False
# True

if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    print(f"Input: {pattern}, {s}")
    print(f"Output: {wordPattern(pattern, s)}")
    
    pattern2 = "aaaa"
    s3 = "dog cat dog cat"
    print(f"Input: {pattern2}, {s3}")
    print(f"Output: {wordPattern(pattern2, s3)}")
    
    s4 = "dog dog dog dog"
    print(f"Input: {pattern2}, {s4}")
    print(f"Output: {wordPattern(pattern2, s4)}")
    
   