# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:31:56 2018

@author: Robi
"""
import math

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __repr__(self):
        return 'Point(%d, %d)' % (self.x, self.y)
        
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError('Expected point to be Point. Got %s' % type(other))
            
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError('Expected point to be Point. Got %s' % type(other))
            
    def __mul__(self, other):
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError('Expected point to be Point or int. Got %s' % type(other))
            
    def __rmul__(self, other):
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError('Expected point to be Point or int. Got %s' % type(other))
            
    def distance(self, other):
        if isinstance(other, Point):
            return math.sqrt(pow((self.x - other.x), 2) + pow((self.y - other.y), 2))
        else:
            raise TypeError('Expected point to be Point. Got %s' % type(other))