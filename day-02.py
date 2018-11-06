# ==== 30-DAY CODING CHALLENGE: DAY 2 ====
#
# Problem:
# Given an array of integers, return a new array such that each element at index i of the new # array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1]
# the expected output would be [2, 3, 6].
#
# Solution written by: Juan Ortiz
# Time complexity for solution: O(n^2)
# ========================================

inputs = [3, 2, 1]

products = []
placeHolder = 0  # the placeholder is used to store, and restore, the removed element

for i, value in enumerate(inputs):
    placeHolder = inputs.pop(i)  # remove element i from the list
    product = 1
    for j in inputs:  # calculate the product of the remaining elements
        product *= j
    products.append(product)
    # restore the placeHolder value back into element i
    inputs.insert(i, placeHolder)
    print(i, value, products)
