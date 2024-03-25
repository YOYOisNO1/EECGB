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
# Write a python function to find sum of product of binomial co-efficients.
#
# SOLUTION CODE
# ============================================
def binomial_Coeff(n,k): 

    C = [0] * (k + 1); 

    C[0] = 1; # nC0 is 1 

    for i in range(1,n + 1):  

        for j in range(min(i, k),0,-1): 

            C[j] = C[j] + C[j - 1]; 

    return C[k]; 

def sum_of_product(n): 

    return binomial_Coeff(2 * n,n - 1); 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(binomial_Coeff(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



