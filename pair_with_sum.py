# ========================================
# Problem:
# Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.
# Assume the list is unordered.
#
# Solution(s) written by: Juan Ortiz
# ========================================

values = [10, 7, 15, 3, 21, 8, 45]
expected_sum = 24

# naive solution : time complexity of O(n^2)
def contains_pair_with_sum_naive(array, expected_sum) -> bool:
    for x in array:  # Loop throw each value
        for y in array[1:]:    # check value against all other values
            if x + y == expected_sum:
                return True
    return False

# better soution: time complexity of O(nlog(n))
def contains_pair_with_sum_better(array, expected_sum) -> bool:
    array.sort()

    first_half = array[:len(array)//2]
    second_half = array[(len(array)//2):]
    for x in first_half:
        for y in second_half:
            sum = x + y
            if sum > expected_sum:
                y -= 1
            elif sum < expected_sum:
                x += 1
            elif sum == expected_sum:
                return True
    return False

print(contains_pair_with_sum_naive(values, expected_sum))
print(contains_pair_with_sum_better(values, expected_sum))