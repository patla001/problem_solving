# Problem 4: Consecutive Characters

# Write a function count_consecutive_characters() that takes in a string str1 as a parameter 
# and returns the count of the most frequent consecutive character.

def count_consecutive_characters(str1):
    if not str1:
        return 0
   
    count = 1
    max_count = 1
    
    for i in range(1, len(str1)):
        if str1[i-1] == str1[i]:
            count += 1
            
            if count > max_count:
                max_count = count
        if str1[i-1] != str1[i]:
            
            count = 1
               
    return max_count


# Example Usage:

# str1 = "aaabbcaaaa"
# count = count_consecutive_characters(str1)
# print(count)
# str2 = "abcde"
# count2 = count_consecutive_characters(str2)
# print(count2)

# Example Output:

# 4
# 1

if __name__ == "__main__":
    str1 = "aaabbcaaaa"
    count = count_consecutive_characters(str1)
    print(f"Input: {str1}")
    print(f"Output: {count}")
    
    str2 = "abcde"
    count2 = count_consecutive_characters(str2)
    print(f"Input: {str2}")
    print(f"Output: {count2}")
