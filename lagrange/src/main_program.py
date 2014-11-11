'''
Created on 11.11.2014

@author: Vladislav
'''
import numpy
from numpy import pi
from math import cos, sin

def mega_f(x):
    return cos(float(x) / 3) - sin(float(x) / 2)

def mega_g(x):
    return cos(5 * float(x))

def construct_Lagrange_polynomial(xs, fs, omega):
    lagrange_poly = [] ## array of lambdas
    for i in xrange(len(fs)):
        x_i = xs[i] ### for convenience
        f_i = fs[i] ### for convenience
        ### getting the copy of all factors to make the omega safe from /0
        new_omega = omega[:] 
        ### do not need the i_th delta, where x_i is subtracted
        new_omega.pop(i) 
        ### get the denominator by substituting x_i in each factor and getting the total product
        denominator = numpy.prod(map(lambda factor_lambda, x_i=x_i, new_omega=new_omega : factor_lambda(x_i), new_omega))
        ### each summand is lambda x :  w(x) * f_i/denominator
        summand_lambda = lambda x, f_i=f_i, denominator=denominator, new_omega=new_omega: float(f_i) / float(denominator) * numpy.prod(map(lambda factor : factor(x), new_omega))
        lagrange_poly.append(summand_lambda)
    return lagrange_poly

def eval_Lagrange(lagrange, x):
    return numpy.sum(map(lambda summand : summand(x), lagrange))      
    

if __name__ == '__main__':
    segment = [-pi/2, pi/2]
    xs = [-pi/3, -pi/5, -pi/9, pi/7, pi/3 ]
    fs = map(lambda x: mega_f(x), xs[:])
    gs = map(lambda x: mega_g(x), xs[:])
    #using the x_i = x_i to make python to close over the value of x_i and not, the name that is "lazy watched" once
    omega = [(lambda x, x_i=x_i : x - x_i) for x_i in xs]
    f_lagrange = construct_Lagrange_polynomial(xs, fs, omega)
    g_lagrange = construct_Lagrange_polynomial(xs, gs, omega)
    print "done"
    print "Lagrange       |        Original"
    for i in range(len(xs)):
        print eval_Lagrange(f_lagrange, xs[i]), " ", fs[i] 
        
    