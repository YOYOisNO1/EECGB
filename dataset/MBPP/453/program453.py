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
# Write a python function to find the sum of even factors of a number.
#
# SOLUTION CODE
# ============================================
import math 

def sumof_factors(n) : 

    if (n % 2 != 0) : 

        return 0

    res = 1

    for i in range(2, (int)(math.sqrt(n)) + 1) :    

        count = 0

        curr_sum = 1

        curr_term = 1

        while (n % i == 0) : 

            count= count + 1

            n = n // i 

            if (i == 2 and count == 1) : 

                curr_sum = 0

            curr_term = curr_term * i 

            curr_sum = curr_sum + curr_term 

        res = res * curr_sum  

    if (n >= 2) : 

        res = res * (1 + n) 

    return res 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(sumof_factors(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



