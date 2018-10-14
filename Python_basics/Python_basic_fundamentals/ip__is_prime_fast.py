# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:59:50 2018

@author: Robi

is_prime function is somewhat slow. 
This is because we are doing a ton of extra work checking modular arithmetic. 
We will use two optimizations to make a is_prime_fast function.

The first optimization takes advantage of the fact that two is the only even prime.
Thus we can check if a number is even and as long as its greater than 2, we know that it is not prime.

Our second optimization takes advantage of the fact that when checking factors, 
we only need to check up the square root of a number. 
Consider a number n decomposed into factors  n=ab . 
There are two cases, either n is prime and without loss of generality, a=n, b=1 or n is not prime and a,b≠n,1. 
In this case, if  a>√n , then  b<√n . So we only need to check all possible values of b and we get the values of a for free!
This means that even the simple method of checking factors will increase in complexity as a square root compared to the size of the number and not linearly.
"""

from math import sqrt
from itertools import count, islice

def is_prime_fast(number):
    if number == 1:
        return False
    
    if (number % 2 == 0) and (not number == 2) :
        return False
    
    for factor in islice(count(2), int(sqrt(number)-1)):
        if number % factor == 0:
            return False

    return True

def get_primes_fast(n):
    prime_list = []
    for number in range(n):
        if is_prime_fast(number):
            prime_list.append(number)
    return prime_list

print(get_primes_fast(100))