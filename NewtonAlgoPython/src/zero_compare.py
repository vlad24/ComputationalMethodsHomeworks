'''
Created on 16.09.2014

@author: Vladislav
'''
from constants import epsilon
def isMoreThan0(x):
    return x > epsilon

def isLessThan0(x):
    return x < -epsilon

def is0(x):
    return not(isMoreThan0(x)) and not(isLessThan0(x))
    