from constants import epsilon, sigma, gamma
from my_functions import f, g, det_x, det_y, det

print ("___Solver loaded")

def find_super_start_points(a,k, xl, xr, yl, yr):
    x = xl
    while (x <= xr):
        y = yl
        while (y <= yr):
            #print (x,y)
            if (abs(f(k,x,y)) <= sigma and abs(g(a,x,y)) <= sigma):
                print("--- Start point found! : ", x , ",", y , "| f = ", f(k,x,y), "g = ", g(a, x, y))
                return [x,y]    
            y += epsilon
        x += epsilon
    return []

def solve_system(a, k, squares):
    print("--- Solving system for a=", a, "| k=", k)
    print("--- Finding start point")
    for square in squares:
            print("--- Solving on ", square)
            super_start = find_super_start_points(a, k, *square)
            print("--- Search has been ended")
            if (super_start != []):
                i = 1
                current = super_start
                previous = [current[0] - 1, current[1] - 1]
                print("i | x                   | y                    | f(x,y)            | g(x,y)           ")
                while not((abs(current[0] - previous[0]) < gamma) and (abs(current[1] - previous[1]) < gamma) ):
                    previous = current
                    xk = current[0]
                    yk = current[1]
                    current = [xk + det_x(a, k, xk, yk) / det(a, k, xk, yk)  ,  yk + det_y(a, k, xk, yk) / det(a, k, xk, yk)  ]
                    print(i, " ", current[0], " ", current[1], " ", f(k, xk, yk), g(a, xk, yk))
                    i += 1
                print("--- Solved : ", current , "(", previous, ")")
            else:
                print("--- No points found")
