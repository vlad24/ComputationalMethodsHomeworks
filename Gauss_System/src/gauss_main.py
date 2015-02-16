import numpy as np

    
def gaussiate_forward(extended_matrix):
    n = extended_matrix.shape[1] - 1
    for iteration in range(n - 1):
        good_row = iteration
        found = False
        #Finding good row for division
        while (good_row < n):
            if extended_matrix[good_row][iteration] != 0:
                found = True
                break
            good_row += 1
        if not found:
            raise Exception("Matrix with det = 0")
        #Swapping columns
        buffer_row = np.copy(extended_matrix[iteration, :])
        extended_matrix[iteration, :] = extended_matrix[good_row, :]
        extended_matrix[good_row, : ] = buffer_row
        #Now the iteration row holds the "row-instrument" - subtract
        iter_a = extended_matrix[iteration, iteration]
        print "taking", iter_a
        for lower in range(iteration + 1, n):
            lower_a = extended_matrix[lower, iteration] 
            extended_matrix[lower, :] -= lower_a * (extended_matrix[iteration, :] / iter_a)
        print "AFTER ITERATION ", 1 + iteration
        print "-----------------------------------Matrix:"
        print extended_matrix
        print "-----------------------------------b vector:"
        print np.sum(extended_matrix, axis=1, keepdims=True)
        print  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
def gaussiate_backwards(extended_matrix):
    try:
        n = extended_matrix.shape[1] - 1
        solutions = np.zeros(n)
        for i in range(n - 1, -1, -1):
            producted = np.multiply(solutions, extended_matrix[i, :-1]).sum()
            solutions[i] = (extended_matrix[i, -1] - producted) / extended_matrix[i,i]
        return np.reshape(solutions, (n,1))
    except:
        print "Error in going backwards"
            
            
    
if __name__ == '__main__':
    extended_matrix = np.array([
                       [5.11, -2.32,  0.46,  1.52,    0,   6.0109],
                       [1.17, -4.08, -3.25,  3.25,  2.34,  0.5958],
                       [0,     1.74,  3.78,  2.15,  1.83,  6.1977],
                       [0,     2.34,  2.05,  -3.5,  1.25, -0.7410],
                       [0,        0,  1.82,  2.67, -4.79,  3.8015]
                      ],dtype=np.float64)
    b_column = np.sum(extended_matrix, axis=1, keepdims=True)
    print "===============At start:"
    print extended_matrix
    print "-----------------------------------b vector:"
    print np.sum(extended_matrix, axis=1, keepdims=True)
    print "==============="
    dirty_matrix = np.copy(extended_matrix)         
    gaussiate_forward(dirty_matrix) 
    solution = gaussiate_backwards(dirty_matrix)
    print "Solution vector:"
    print solution
    print "Difference:", np.sum((np.absolute((np.dot(extended_matrix[:,:-1], solution) - np.reshape(extended_matrix[:,-1], (-1,1))))))

            
    
    