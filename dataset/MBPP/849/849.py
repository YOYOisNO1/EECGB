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
# Write a python function to find sum of all prime divisors of a given number.
#
# SOLUTION CODE
# ============================================
def sum(N): 

    sumOfPrimeDivisors = [0]*(N + 1)   

    for i in range(2,N + 1) : 

        if (sumOfPrimeDivisors[i] == 0) : 

            for j in range(i,N + 1,i) : 

                sumOfPrimeDivisors[j] += i           

    return sumOfPrimeDivisors[N] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(sum(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



