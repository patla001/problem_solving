#!/bin/python

# Write a function reverse_only_letters() that takes in a string s as a parameter. 
# The function reverses the order of the letters in the string and returns the new string. 
# Non-letter characters should remain in their original positions.

def reverse_only_letters(s):
    
    # traverse the UpperCase list with s list
    n = len(s)
    lst = []
    for i in s:
        # check the alphabet
        if i.isalpha():
            # append the character to the list
            lst.append(i)
        # reverse the list
        lstchar = lst[::-1]
    
    char = ""
    count = 0
    # traverse again the reverse list
    for k in lstchar:
        # check the character is alphabet or not
        if s[count] == '-':
            # add the hiphen to the string
            char = char+s[count]
        else:
            # add the character to the string
            char = char+k
        count = count + 1
    return char

# Example Usage:

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)

# Example Output: j-Ih-gfE-dCba

if '__main__' == __name__:
    s = "a-bC-dEf-ghIj"
    print(f'Input: {s}')
    reversed_s = reverse_only_letters(s)
    print(f'Output: {reversed_s}')