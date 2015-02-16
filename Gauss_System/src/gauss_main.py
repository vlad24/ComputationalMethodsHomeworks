import numpy as np

    
def gaussiate_forward(matrix):
    n = matrix.shape[1] - 1
    for iteration in range(n - 1):
        good_row = iteration
        found = False
        #Finding good row for division
        while (good_row < n):
            if matrix[good_row][iteration] != 0:
                found = True
                break
            good_row += 1
        if not found:
            raise Exception("Matrix with det = 0")
        #Swapping columns
        buffer_row = np.copy(matrix[iteration, :])
        matrix[iteration, :] = matrix[good_row, :]
        matrix[good_row, : ] = buffer_row
        #Now the iteration row holds the "row-instrument" - subtract
        iter_a = matrix[iteration, iteration]
        for lower in range(iteration + 1, n):
            lower_a = matrix[lower, iteration] 
            matrix[lower, :] -= lower_a * (matrix[iteration, :] / iter_a)
        print "AFTER ITERATION ", 1 + iteration
        print "---Matrix:"
        print matrix
        print "---b vector:"
        print np.sum(matrix, axis=1, keepdims=True)
        print  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
def gaussiate_backwards(matrix):
    try:
        n = matrix.shape[1] - 1
        solutions = np.zeros(n)
        for i in range(n - 1, -1, -1):
            producted = np.multiply(solutions, matrix[i, :-1]).sum()
            solutions[i] = (matrix[i, -1] - producted) / matrix[i,i]
        return np.reshape(solutions, (n,1))
    except:
        print "Error in going backwards"
            
            
    
if __name__ == '__main__':
    matrix = np.array([
                       [1,2,1,2],
                       [4,8,5,8],
                       [3,7,3,6]
                      ],dtype=np.float64)
    b_column = np.sum(matrix, axis=1, keepdims=True)
    print "===============At start:"
    print matrix
    print "---b vector:"
    print np.sum(matrix, axis=1, keepdims=True)
    print "==============="
    dirty_matrix = np.copy(matrix)         
    gaussiate_forward(dirty_matrix) 
    solution = gaussiate_backwards(dirty_matrix)
    print "Solution:"
    print solution
    print "Difference:", np.sum((np.absolute((np.dot(matrix[:,:-1], solution) - np.reshape(matrix[:,-1], (-1,1))))))

            
    
    