#!/usr/bin/env python
"""
    A list is symmetric if the first row is the same as the first column,
    the second row is the same as the second column and so on. Write a
    procedure, symmetric, which takes a list as input, and returns the
    boolean True if the list is symmetric and False if it is not.
"""
def symmetric(symmetric_list):
    """
    Validate symetric list by its entries
    """
    if valid_symetric(symmetric_list):
        length_list = len(symmetric_list)
        i = 0 # index for row/colum
        while i < length_list: #through each row/column
            j = 0
            while j < length_list:
                if symmetric_list[i][j] == symmetric_list[j][i]:
                    j += 1
                else:
                    return False
            i += 1
        return True
    return False

def valid_symetric(symmetric_list):
    """
    validates the size of a symmetric array
    """
    symmetric_length = len(symmetric_list)
    for row in symmetric_list:
        if len(row) != symmetric_length:
            return False
    return True

print(symmetric([[1, 2, 3], \
                  [2, 3, 4],\
                  [3, 4, 1]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]]))
# #>>> True

print(symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "dog"],
               ["fish","fish","cat"]]))
# #>>> False

print(symmetric([[1, 2],
               [2, 1]]))
# #>>> True

print(symmetric([[1, 2, 3, 4],\
                  [2, 3, 4, 5],\
                  [3, 4, 5, 6]]))
# #>>> False

print(symmetric([[1, 2, 3],
                 [2, 3, 1]]))
