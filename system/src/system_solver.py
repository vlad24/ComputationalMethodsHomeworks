from constants import epsilon, sigma, gamma
from my_functions import f, g, det_x, det_y, det
import tabulate

print  ("___Solver loaded")

def find_super_start_points(a,k, x_left, x_right, y_down, y_up):
    x = x_left
    while (x <= x_right):
        y = y_down
        while (y <= y_up):
            #print (x,y)
            if (abs(f(k,x,y)) <= sigma and abs(g(a,x,y)) <= sigma):
                print "--- Start point found! : ", x , ",", y , "; f = ", f(k,x,y), " ; g = ", g(a, x, y)
                return [x, y]    
            y += epsilon
        x += epsilon
    return []

def solve_system(a, k, squares):
    print "--- Solving system for a=", a, "| k=", k
    print "f(x,y) = ", "exp(", k ," * x + y) - x*y - 1.4"
    print "g(x,y) = ", "(x^2)/", "(", a, "^2) + 2*(y^2) - 4"
    print "--- Finding start points..."
    solutions = []
    for square in squares:
        print "--- Solving on ", square
        super_start = find_super_start_points(a, k, *square)
        print "--- Search has been ended"
        if (super_start != []):
            i = 1
            current = super_start
            previous = [current[0] - 1, current[1] - 1]
            table_head = ["i", "x", "y", "f(x, y)", "g(x, y)"]
            rows = []
            while not((abs(current[0] - previous[0]) < gamma) and (abs(current[1] - previous[1]) < gamma) ):
                previous = current
                x_k = current[0]
                y_k = current[1]
                current = [x_k + det_x(a, k, x_k, y_k) / det(a, k, x_k, y_k)  ,  y_k + det_y(a, k, x_k, y_k) / det(a, k, x_k, y_k)  ]
                row = [i, current[0],  current[1], f(k, x_k, y_k), g(a, x_k, y_k)]
                rows.append(row)
                i += 1
            print tabulate.tabulate(rows, table_head, "rst")
            print "--- Solved : ", current
            solutions += current
        else:
            print "--- No points found!"
    print "---SOLUTIONS: ", solutions
        
