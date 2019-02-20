# ========================================
# Problem:
# Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.
#
# Solution written by: Juan Ortiz
# Time complexity for solution: O(n^2)
# ========================================

values = [10, 15, 3, 7]
k = 17


def has_sum_of_key(array, key):
    ''' returns True if there exists a pair of values within the array that summate to the argued key.'''
    for x in array:  # Loop throw each value
        for y in array[1:]:    # check value against all other values
            if x + y == key:
                print(x, "+", y, "=", sum)
                return True
    print("No pairs equal to", key)
    return False


print(has_sum_of_key(values, k))
