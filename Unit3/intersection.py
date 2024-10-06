#!/bin/python

# Write a function dict_intersection() that takes in two dictionaries as parameters 
# and returns a new dictionary containing the key-value pairs found in both dictionaries.

def dict_intersection(d1, d2):
    #intersection = {}
    intersection = d1.items() & d2.items()
    # for k, v in d1.items():
    #     if k in d2 and v == d2[k]:
    #         intersection[k] = v
    #         return intersection
    return intersection
        

# Example Input:

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 4}

# Example Output: {'b': 2}

if '__main__' == __name__:
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'b': 2, 'c': 4}
    print(dict_intersection(d1, d2))