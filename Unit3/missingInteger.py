#/bin/python

# Problem 2: Missing Integer

# Write a function find_missing_positive() that takes in 
# a sorted list of integers nums that always starts at 1, 
# and returns the smallest missing positive integer.

def find_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        print(f'nums[i]: {nums[i]} i: {i+1}')
        if nums[i] != i + 1:
            # it retuns the next number if the element is missing.
            return i + 1
    # it outputs the next number if the list is sorted.
    return n + 1



# Example Usage:

# nums1 = [1,2,3,5,6,10]
# print(find_missing_positive(nums1))

# nums2 = [1,2,3,4,5]
# print(find_missing_positive(nums2))

# Example Output:

# 4
# 6

if __name__ == "__main__":
    nums1 = [1,2,3,5,6,10]
    print(f"Input: {nums1}")
    print(f"Output: {find_missing_positive(nums1)}")
    
    nums2 = [1,2,3,4,5]
    print(f"Input: {nums2}")
    print(f"Output: {find_missing_positive(nums2)}")
    
    