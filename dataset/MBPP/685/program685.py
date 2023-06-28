import array
import bisect
import collections
import datetime
import functools
import heapq
import itertools
import math
import queue
import re
import string
import sys
from typing import Any, Dict, List, Optional, Set

# Question Prompt (NOT what is passed to the model)
# Write a python function to find sum of prime numbers between 1 to n.
#
# SOLUTION CODE
# ============================================
def sum_of_primes(n): 

    prime = [True] * (n + 1)  

    p = 2

    while p * p <= n: 

        if prime[p] == True:  

            i = p * 2

            while i <= n: 

                prime[i] = False

                i += p 

        p += 1    

    sum = 0

    for i in range (2,n + 1): 

        if(prime[i]): 

            sum += i 

    return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(sum_of_primes(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



