# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:49:48 2018

@author: Robi

We can test if a Mersenne number is prime using the Lucas-Lehmer series. 
First let's write a function that generates the series. 
Given a Mersenne number with exponent p, the series can be defined as

n0=4
ni=(n2i−1−2)mod(2p−1)

"""

def lucas_lehmer(p):
    ll_list = [4]
    for i in range(1, p-1):
        n = (((ll_list[i-1])**2)-2) % ((2**p)-1)
        ll_list.append(n)
    return ll_list

print(lucas_lehmer(17))