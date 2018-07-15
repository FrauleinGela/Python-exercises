"""By Dimitris_GR from forums
Modify Problem Set 31's (Optional) Symmetric Square to return True 
if the given square is antisymmetric and False otherwise. 
An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
for each i=0,1,...,n-1 and for each j=0,1,...,n-1."""

def antisymmetric(symmetric_list):
    """
    Validate symetric list by its entries
    """
    if valid_symetric(symmetric_list):
        length_list = len(symmetric_list)
        i = 0 # index for row/colum
        while i < length_list: #through each row/column
            j = 0
            while j < length_list:
                if symmetric_list[i][j] == -symmetric_list[j][i]:
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

print(antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]]))

#>>> True

print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]]))
#>>> False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False
