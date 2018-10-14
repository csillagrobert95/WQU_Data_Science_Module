# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:28:29 2018

@author: Robi
"""

from point import Point

class Cluster(object):
    def __init__(self, x, y):
        self.center = Point(x, y)
        self.points = []
    
    def update(self):
        x_total = 0
        y_total = 0
        for point in self.points:
            x_total += point.x
            y_total += point.y
        self.center = Point(x_total / len(self.points), y_total / len(self.points))
    
    def add_point(self, point):
        self.points.append(point)
        
def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    b_old = []
    for _ in range(10000): # max iterations
        a_new = Cluster(0,0)
        a_new.center = a.center
        b_new = Cluster(0,0)
        b_new.center = b.center
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                # add the right point
                a_new.add_point(point)
            else:
                # add the right point
                b_new.add_point(point)
        if a_old == a_new.points or b_old == b_new.points:
            break
        a_old = a_new.points
        b_old = b_new.points
        a.points = a_new.points
        b.points = b_new.points
        a.update()
        b.update()

    print ('A points: ', a.points)
    print ('B points: ', b.points)
    print ('A center: ', (a.center.x,a.center.y))
    print ('B center: ', (b.center.x,b.center.y))
    if a.center.x > b.center.x:
        return [(a.center.x,a.center.y),(b.center.x,b.center.y)]
    else:
        return [(b.center.x,b.center.y),(a.center.x,a.center.y)]
    
compute_result([(1,2),(-2,3),(-5,7),(3,4),(-7,-1),(-10,5),(0,0)])