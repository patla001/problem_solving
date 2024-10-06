#!/bin/python
# Problem 3: Longest Common Prefix

# Write a function longest_common_prefix() that takes 
# in a list of strings strings as a parameter. 
# The function returns the longest common prefix (not substring) 
# of all strings and if there are none, it returns an empty string "".

def longest_common_prefix(strings):
    if not strings:
        return ""
    #print(strings[1:])
    for i in range(len(strings[0])):
        for string in strings[1:]:
            if i >= len(string) or string[i] != strings[0][i]:  
                return strings[0][:i]

    return strings[0]


# Example Usage:

# strings = ["flower", "flow", "flight"]
# common_string = longest_common_prefix(strings)
# print(common_string)

# strs = ["dog", "racecar", "car"]
# common_str = longest_common_prefix(strs)
# print(common_str)

# Example Output:

# fl

if __name__ == "__main__":
    strings = ["flower", "flow", "flight"]
    common_string = longest_common_prefix(strings)
    print(f"Input: {strings}")
    print(f"Output: {common_string}")

    strs = ["dog", "racecar", "car"]
    common_str = longest_common_prefix(strs)
    print(f"Input: {strs}")
    print(f"Output: {common_str}")