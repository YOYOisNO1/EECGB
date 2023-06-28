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
# Write a python function to count the number of distinct power of prime factor of given number.
#
# SOLUTION CODE
# ============================================
def count_fac(n):  

    m = n 

    count = 0

    i = 2

    while((i * i) <= m): 

        total = 0

        while (n % i == 0): 

            n /= i 

            total += 1 

        temp = 0

        j = 1

        while((temp + j) <= total): 

            temp += j 

            count += 1

            j += 1 

        i += 1

    if (n != 1): 

        count += 1 

    return count 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(count_fac(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



