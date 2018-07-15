correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]
incorrect1 = [[1,2],[1]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
incorrect6 = [[0,1,2],
                [2,0,1],
                [1,2,0]]
               

def check_sudoku(sudoku):
    # through each digit
    max_digit = len(sudoku)
    # start from first digit, and find if it is repeated on each row/column
    digit = 1
    i = 0
    j = 0
    while digit <= max_digit:
        i = 0
        j = 0
        while i < max_digit: #through each column/row
            digitRow = 0
            digitColumn = 0
            while j < max_digit:
                if sudoku[i][j] == digit:
                    digitRow += 1
                if sudoku[j][i] == digit:
                    digitColumn += 1
                j += 1
            if digitRow != 1 or digitColumn != 1: # sudoku is not valid, found more than one the same number
                return False
            i += 1
            j = 0
        digit += 1 
    return True
    
    
print check_sudoku(incorrect1)
print check_sudoku(correct)