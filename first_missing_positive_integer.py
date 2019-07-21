# ========================================
# Problem:
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain  duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3. You can modify the input array in-place.
#
# Solution(s) written by: Juan Ortiz
# ========================================

# Time complexity for solution: O(n)
def fmpi(numbers):
    '''
    returns first missing positive integer in a list
    '''
    high = max(numbers)

    if high < 1:
        return 1

    if len(numbers) == 1:
        return 2 if numbers[0] == 1 else 1

    missing = [0] * high

    for i in range(len(numbers)):
        if numbers[i] > 0:
            if missing[numbers[i] - 1] != 1:
                missing[numbers[i] - 1] = 1

    for i in range(len(missing)):
        if missing[i] == 0:
            return i + 1
    return i + 2

sequence = [3, -1, 0]
print(fmpi(sequence))
