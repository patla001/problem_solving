#!/bin/python

# Problem 5: Partition Labels

# Write a function partition_labels() that takes in a string s as a parameter. 
# s consists of lowercase letters 
# and represents the order of characters as they appear in a document. 
# The function partitions s into as many parts as possible 
# so that each unique letter appears in at most one part, 
# and returns a list of integers representing the size of these parts.

def partition_label(s):
    last = {char: i for i, char in enumerate(s)}
    #print(last)
    start = 0
    end = 0
    result = []
    
    for i, char in enumerate(s):
        end = max(end, last[char])
        
        if i == end:
         
            #print(f'index i: {i} start: {start} end: {end} last[{char}]: {last[char]}')
            result.append(end - start + 1)
            #print(result)
            start = i + 1
    #return -1        
    return result

# Example Usage:

# s1 = "ababcbacadefegdehijhklij"
# print(partition_label(s1))

# s2 = "abcabcbadefffeda"
# print(partition_label(s2))

# Example Output:

# # s1 partitioned into "ababcbaca", "defegde" and "hijhklij"
# [9, 7, 8]
# # s2 cannot be partitioned into more parts because of the "a" character at the end
# [16]

if __name__ == "__main__":
    s1 = "ababcbacadefegdehijhklij"
    print(f"Input: {s1}")
    print(f"Output: {partition_label(s1)}")

    s2 = "abcabcbadefffeda"
    print(f"Input: {s2}")
    print(f"Output: {partition_label(s2)}")