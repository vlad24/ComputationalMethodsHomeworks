'''
Created on 11.11.2014

@author: Vladislav
'''
import numpy
import tabulate
from numpy import pi
from math import cos, sin, factorial
from constants import part_amount, dif_h, small_step
from numpy.matlib import rand
from dff.modules.viewer.hexedit.goto import goto

 

def nth_dif_of_sin(n, arg_coef):
    #0: sin; 1 : cos; 2 : -sin 3: -cos
    neg_one_factor = 1
    if (n % 4 == 0):
        neg_one_factor = 1
        trig = lambda x: sin(x)
    elif (n % 4 == 1):
        neg_one_factor = 1
        trig = lambda x: cos(x)
    elif (n % 4 == 2):
        neg_one_factor = -1
        trig = lambda x: sin(x)
    else:
        neg_one_factor = -1
        trig = lambda x: cos(x)
    return (lambda x,n=n, neg_one=neg_one_factor, arg_coef=arg_coef, trig=trig: arg_coef**n * neg_one * trig(arg_coef*x))

def nth_dif_of_cos(n, arg_coef):
    #0: cos; 1 : -sin; 2 : -cos 3: sin
    neg_one_factor = 1
    if (n % 4 == 0):
        neg_one_factor = 1
        trig = lambda x: cos(x)
    elif (n % 4 == 1):
        neg_one_factor = -1
        trig = lambda x: sin(x)
    elif (n % 4 == 2):
        neg_one_factor = -1
        trig = lambda x: cos(x)
    else:
        neg_one_factor = 1
        trig = lambda x: sin(x)
    return (lambda x,n=n, neg_one=neg_one_factor, arg_coef=arg_coef, trig=trig: arg_coef**n * neg_one * trig(arg_coef*x))
    
def mega_f(x):
    return cos(float(x) / 3) - sin(float(x) / 2)

def mega_g(x):
    return cos(5 * float(x))

def stupid_max(f, x_segment):
    max_val = -float("infinity")
    e = 0
    print "f(0) = ", f(0), "x[le] = ", x_segment[0], "x[ri] = ", x_segment[-1]
    points = numpy.arange(x_segment[0], x_segment[-1], small_step)
    for p in points:
        tmp = f(p)
        if tmp > max_val:
            max_val = tmp
            e = p
    print "Point: ", e
    return max_val


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
      
def print_table(segment, h, function, l, A):
    points = numpy.arange(segment[0], segment[-1], h)
    table_head = ["x_k", "function(x_k)", "L_5(x_k, function)", "|function(x_k) - L_5(x_k, function)|", "A(x_k)"]
    rows = []
    for point in points:
        t = eval_Lagrange(l, point)
        row = [point, function(point), t, abs(function(point) - t), A(point)]
        rows.append(row)
    print tabulate.tabulate(rows, table_head, "grid")

    
def print_table_at_segment_for_g_and_fs(x_segment, xs):
    fs = map(lambda x: mega_f(x), xs[:])
    gs = map(lambda x: mega_g(x), xs[:])
    #using the x_i = x_i to make python to close over the value of x_i and not, the name that is "lazy watched" once
    omega = [(lambda x, x_i=x_i : x - x_i) for x_i in xs]
    f_lagrange = construct_Lagrange_polynomial(xs, fs, omega)
    g_lagrange = construct_Lagrange_polynomial(xs, gs, omega)
    print "Lagrange       |        Original"
    for i in range(len(xs)):
        print eval_Lagrange(g_lagrange, xs[i]), " ", gs[i] 
    # our interpolation degree 
    n = len(omega)
    # prepare lambda functions for absolute of (n+1 derivatives) of f and g
    abs_nth_der_f = lambda x, n=n, der1=nth_dif_of_cos(n + 1, float(1)/3), der2=nth_dif_of_sin(n + 1, float(1)/2):    abs(der1(x) - der2(x))
    abs_nth_der_g = lambda x,n=n, g1=nth_dif_of_cos(n + 1, float(5)) :     abs(g1(x))
    #calculate their max values
    max_f_der_value = stupid_max(abs_nth_der_f, x_segment)
    max_g_der_value = stupid_max(abs_nth_der_g, x_segment)
    print abs_nth_der_f(0)
    print "Max values: |f`|", max_f_der_value, " ; |g`",n,"|", max_g_der_value
    #construct As
    A_f = lambda x : (abs(numpy.prod(map(lambda factor : factor(x), omega))) * max_f_der_value) / float(factorial(n + 1))
    A_g = lambda x : (abs(numpy.prod(map(lambda factor : factor(x), omega))) * max_g_der_value) / float(factorial(n + 1))
    # prepare yourself for iterating
    h = float(x_segment[-1] - x_segment[0]) / float(part_amount)
    print h
    #Print the target tables
    header = "-" * 11 + "Table for F at" + str(x_segment) + "-" *11
    print header
    print "-" * len(header)
    print_table(x_segment, h, mega_f, f_lagrange, A_f)
    print "-" * len(header)
    print
    header = "-" * 11 + "Table for G at" + str(x_segment) + "-" * 11
    print header
    print "-" * len(header)
    print_table(x_segment, h, mega_g, g_lagrange, A_g)
    print "-" * len(header)
    
    
def experiment_with_xs_at_segment(segment, xs):
    print "1.Original ", xs
    print_table_at_segment_for_g_and_fs(segment, xs)
    
    xs_lefter = map(lambda x : x / float(2), xs[:len(xs)/2])
    print "2.Lefter ", xs_lefter
    print_table_at_segment_for_g_and_fs(segment, xs_lefter)
    
    xs_righter = map(lambda x : 1.1 * x, xs[len(xs)/2 + 1:])
    print "3.Righter. ", xs_righter
    print_table_at_segment_for_g_and_fs(segment, xs_righter)
    
    xs_centered = map(lambda x : x / float(2), xs[len(xs)/2 - 2: len(xs)/2 + 2])
    print "4.Centered. ", xs_centered
    print_table_at_segment_for_g_and_fs(segment, xs_centered)
    
    
    
    
    
if __name__ == '__main__':
    print "*******Main started"
    print "***Experimenting with different segment lengths and number of nodes there"
    segment = [-pi/2, pi/2]
    xs = [-pi/3, -pi/5, -pi/9, pi/7, pi/3]
    experiment_with_xs_at_segment(segment, xs)
    
    
    
    
    
    