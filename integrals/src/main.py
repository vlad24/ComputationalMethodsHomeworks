'''
Created on 26.11.2014

@author: Vladislav
'''

import numpy
from sympy.core.symbol import Symbol
from sympy.functions.elementary.hyperbolic import sinh
from sympy.utilities.lambdify import lambdify


integral_a = 0
integral_b = 0.4
small_step = 1E-3

def brute_max(f, x_segment, debug=False):
    max_val = -float("infinity")
    if debug:
        max_point = 0
    points = numpy.arange(x_segment[0], x_segment[-1], small_step)
    for point in points:
        tmp = f(point)
        if tmp > max_val:
            max_val = tmp
            if debug:
                max_point = point
    if debug:
        print max_point
    return max_val

def integral(formula, f, a, b, n):
    h = (b - a) / float(n)
    if formula == "rect":
        accumulator = 0
        for j in xrange(1, n + 1):
            accumulator += f(a + (2 * j - 1) * (float(h) / 2))
        return h * accumulator
    elif formula == "trap":
        accumulator = (f(a) + f(b)) / 2
        for j in xrange(1, n):
            accumulator += f(a + j * h)
        return h * accumulator
    elif formula == "simp":
        accumulator = (f(a) + f(b)) / 2 + f(a + h/2) * 2
        for j in xrange(1, n):
            accumulator += 2 * f(a + ((2*j + 1) / 2) * h) + f(a + j * h)
        return (h / 3) * accumulator
    
def remainder(formula, f, a, b, n, der2_f=None, der4_f=None):
    if formula == "rect" and der2_f is not None:
        m1 = ( ((b - a)**3) / (24 * n**2) )
        m2 = brute_max(der2_f, [a, b])
        return abs(m1 * m2) 
    elif formula == "trap" and der2_f is not None:
        m1 = ( ((b - a)**3) / (12 * n**2) )
        m2 = brute_max(der2_f, [a, b])
        return abs(m1 * m2) 
    elif formula == "simp" and der4_f is not None:
        m1 = ( -((b - a)**3) / (2880 * n**4) )
        m2 = brute_max(der4_f, [a, b])
        return abs(m1 * m2)
    
def runge(k, I_2n, I_n):
    return float(((1 << k) * I_2n - I_n)) / ((1 << (k - 1)) - 1) 

if __name__ == '__main__':
    x = Symbol('x')
    f_expression = 1 / (0.3 + sinh(x))
    der2_f_expression = f_expression.diff(x, 2) 
    der4_f_expression = f_expression.diff(x, 4)
    f = lambdify(x, f_expression)
    der2_f = lambdify(x, der2_f_expression)
    der4_f = lambdify(x, der4_f_expression)
    formula_ks = {"rect":2, "trap":2, "simp":4}
    values = dict()
    for formula in ("rect", "trap", "simp"):
        values[formula] = dict()
        for integral_n in (8, 16):
            values[formula][integral_n] = dict()
            I = integral(formula, f, integral_a, integral_b, integral_n)
            r = remainder(formula, f, integral_a, integral_b, integral_n, der2_f, der4_f)
            values[formula][integral_n]["value"] = I ; values[formula][integral_n]["remainder"] = r
        I_runge = runge(formula_ks[formula], values[formula][16]["value"], values[formula][8]["value"])
        values[formula]["runge"] = I_runge
    #print values
    
    for formula in values.iterkeys():
        print "---", formula
        print " "*8, "runge precisicion =", values[formula]["runge"]
        for n in values[formula].iterkeys():
            if type(n) is int:
                print " "*16, "n =", n
                for value in values[formula][n].iterkeys():
                    print " "*24, value ,"=", values[formula][n][value]
        
    