# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:15:50 2018

@author: Robi

Sieve of Eratosthenes

1. Generate a list of all numbers between 2 and N
2. Starting with p=2 (the first prime) mark all numbers of the form  np  where
n>1  and np<=N to be not prime (they can't be prime since they are multiples of 2!)
3. Find the smallest number greater than p which is not marked and set that equal to p, then go back to step 2.
Stop if there is no unmarked number greater than  pp  and less than  N+1
"""

from itertools import repeat

def list_true(n):
    list_tr = [False, False]
    list_tr = list_tr + list(repeat(True, n-1))
    return list_tr

#takes a list of elements and a number p and marks elements false which are in the range 2p,3p...N
def mark_false(bool_list, p):
    for num in range(2, len(bool_list)):
        if(num*p) < len(bool_list):
            bool_list[num*p] = False
    return bool_list        

#returns the smallest element in a list which is not false and is greater than p.          
def find_next(bool_list, p):
    if (p < len(bool_list)):
        for ind in range(p+1, len(bool_list)):
            if bool_list[ind] is not False:
                return ind

#given a list of True and False, return the index of the true values.
def prime_from_list(bool_list):
    true_val = []
    for ind in range(len(bool_list)):
        if bool_list[ind] is True:
            true_val.append(ind)
    return true_val

def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)

print(sieve(200))