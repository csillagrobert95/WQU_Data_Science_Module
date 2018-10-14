# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 13:11:25 2018

@author: Robi

A Mersenne number is any number that can be written as 2p−1 for some p.
For example, 3 is a Mersenne number (2^2−1) as is 31 (2^5−1).

Write a function that accepts an exponent p and returns the corresponding Mersenne number.
"""

def mersenne_number(p):
    return (2**p) - 1


def is_prime(number):
    if number == 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True

def get_primes(n_start, n_end):
    prime_list = []
    for number in range(n_start, n_end+1):
        if is_prime(number):
            prime_list.append(number)
    return prime_list

    
def return_mersenne():
    mersenne_list = []
    primes_list = get_primes(3,65)
    for number in primes_list:
        mersenne_list.append(mersenne_number(number))
    return mersenne_list

print (return_mersenne())