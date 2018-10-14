# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:39:44 2018

@author: Robi

For a given Mersenne number with exponent  p , the number is prime if the Lucas-Lehmer series is 0 at position p−2.
Write a function that tests if a Mersenne number with exponent  p  is prime.
Test if the Mersenne numbers with prime  p  between 3 and 65 (i.e. 3, 5, 7, ..., 61) are prime.
Your final answer should be a list of tuples consisting of (Mersenne exponent, 0) (or 1) for each Mersenne number you test, where 0 and 1 are replacements for False and True respectively.
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

def ll_prime(p):
    s = 4
    m = (2**p) - 1
    for i in range(1, p-1):
        s = ((s**2) - 2) % m
    if s == 0:
        return 1
    else:
        return 0

def prime_test_results():
    primes_list = get_primes(3,65)
    ll_list = []
    for number in primes_list:
        ll_list.append(ll_prime(number))
    return list(zip(primes_list, ll_list))

print (prime_test_results())
