# Rutronik Elektronische Bauelemente GmbH Disclaimer: The evaluation board
# including the software is for testing purposes only and,
# because it has limited functions and limited resilience, is not suitable
# for permanent use under real conditions. If the evaluation board is
# nevertheless used under real conditions, this is done at one’s responsibility;
# any liability of Rutronik is insofar excluded

def apply_offset(y, offset):
    retval = []
    for i in range(len(y)):
        retval.append(y[i] + offset)
    return retval

def mult_array(a, b):
    retval = []
    for i in range(len(a)):
        retval.append(a[i] * b[i])
    return retval

def array_sum(a, b):
    retval = []
    for i in range(len(a)):
        retval.append(a[i] + b[i])
    return retval

def multiply(y, factor):
    retval = []
    for i in range(len(y)):
        retval.append(y[i] * factor)
    return retval

def get_matrix_max_with_index(matrix):
    maxValue = matrix[0][0]
    maxI = 0
    maxJ = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] > maxValue):
                maxValue = matrix[i][j]
                maxI = i
                maxJ = j
    return maxValue, maxI, maxJ