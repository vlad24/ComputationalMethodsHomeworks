import system_solver
if __name__ == '__main__':
    j = 0
    for i_a in range(6):
        a = 0.7 + 0.1 * i_a
        #0.7, 0.8, ..., 1.3
        for i_k in range(5):
            j += 1
            k = -0.10 - 0.05 * i_k
            #-0.10, - 0.15, .. -0.35
            print "###",j,"### A and K have been chosen : ", a, " ", k
            squares = [[0,2,0,2],[-4,0,-4,0]]
            system_solver.solve_system(a, k, squares)