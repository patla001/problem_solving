# Problem 5: Teemo's Attack

# In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. 
# Write a function find_poisoned_duration() that takes in two parameters: 
# time_series (the time at which Teemo's attacks hits Ashe) and 
# time_duration (the duration of the poisoning effect). 
# The function returns the total time that Ashe is in a poisoned condition.

# time_series is a list of integers that represents 
# the times at which Teemo attacks and 
# makes Ashe poisoned for the exact time_duration.

# If Teemo hits Ashe while she is still poisoned, 
# the poison's duration starts over. 
# For example, if Teemo attacks at times 1 and 4 for 3 seconds, 
# the states at each time would be:

# 1: attacked
# 2: in poison state
# 3: in poison state
# 4: attacked, poison duration resets to 3
# 5: in poison state
# 6: in poison state
# 7: in poison state 
# 8: in normal state

# 9: attacked
# 10: in poison state
# 11: in poison state
# 12: in poison state
# 13: in normal state

# This means that the total time that Ashe is in a poisoned condition is 5.
from itertools import tee
def find_poisoned_duration(time_series, duration):
    n = len(time_series)
    # helper function to iterate over the list
    # consecutive pairs of elements
    def pairwise(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)
    
    # if there are no time stamps the poison duration is 0
    if not time_series:
        return 0
    # initialize the total duration with the duration of the last poison event
    total_duration = duration
    # calculate the total time that Ashe is in a poisoned condition
    for i, j in pairwise(time_series):
        time_diff = j - i
        total_duration += min(duration, time_diff)

    return total_duration - 1


# Example Usage:

# 4 - 1 = 3 < 3
# 9 - 4 = 5 < 3
# duration 5

# time_series = [1,4,9]
# damage = find_poisoned_duration(time_series, 3)
# print(damage)

# 1: attacked
# 2: in poison state
# 3: in poison state
# 4: attacked, poison duration resets to 3
# 5: in poison state
# 6: in poison state
# 7: in poison state 
# 8: in normal state
# 9: attacked
# 10: in poison state
# 11: in poison state
# 12: in poison state
# 13: in normal state


# 4 - 1 = 3 < 3
# 9 - 4 = 5 < 3
# duration 5
# 

# Example Output: 8

if __name__ == '__main__':
    time_series = [1,4]
    damage = find_poisoned_duration(time_series, 3)
    print(f"Input: {time_series}")
    print(f"Output: Total time that Ashe is in a poisoned condition {damage}")

    time_series = [1,4,9]
    damage = find_poisoned_duration(time_series, 3)
    print(f"Input: {time_series}")
    print(f"Output: Total time that Ashe is in a poisoned condition {damage}")